import httpx
from models.lead import Lead
from models.lead_data import LeadData
from models.setting import Setting
from models.advertiser import Advertiser
from models.affiliate import Affiliate
from models.compaign import Compaign
from models.contact import Contact
from models.data_update_log import DataUpdateLog
from models.offer import Offer
from models.verticle import Verticle
import asyncio
import datetime


async def fetch_data(method: str, url: str, **kwargs):
    async with httpx.AsyncClient() as client:
        retry = 3
        while retry > 0:
            try:
                response = await getattr(client, method)(url, **kwargs)
                json_response = response.json()
                return json_response
            except:
                retry -= 1
        return {}


async def fetch_leads():

    json_response = await fetch_data(
        "post",
        "https://api.leadspedia.com/core/v2/leads/getAll.do",
        headers={
            "Authorization": "Basic MmNjYzE2NzY5YjFhYWMwMmY5MDJjNDY3NzM4NTE2NjU6MGM1NWZjMzFjZTU0NTQ4NGY5M2QyMzM3ZDhhNjJiNzQ="
        },
        data={
            "fromDate": (await Setting.filter(key="from_date").first()).value,
            "endDate": (await Setting.filter(key="end_date").first()).value,
            "limit": 1000,
        },
    )
    if not json_response["success"]:
        return False
    await Lead.all().delete()
    for row in json_response["response"]["data"]:
        new_lead = Lead(**row)
        await new_lead.save()
    return True


async def fetch_yearly_leads():
    current_datetime = datetime.datetime.now()
    json_response = await fetch_data(
        "post",
        "https://api.leadspedia.com/core/v2/leads/getAll.do",
        headers={
            "Authorization": "Basic MmNjYzE2NzY5YjFhYWMwMmY5MDJjNDY3NzM4NTE2NjU6MGM1NWZjMzFjZTU0NTQ4NGY5M2QyMzM3ZDhhNjJiNzQ="
        },
        data={
            "fromDate": (current_datetime - datetime.timedelta(days=365)).strftime(
                "%Y-%m-%d"
            ),
            "endDate": current_datetime.strftime("%Y-%m-%d"),
            "limit": 1000,
        },
    )
    if not json_response["success"]:
        return False
    await Lead.all().delete()
    for row in json_response["response"]["data"]:
        new_lead = Lead(**row)
        await new_lead.save()
    return True


import datetime


async def fetch_weekly_leads():
    current_datetime = datetime.datetime.now()
    start_of_week = current_datetime - datetime.timedelta(days=7)
    json_response = await fetch_data(
        "post",
        "https://api.leadspedia.com/core/v2/leads/getAll.do",
        headers={
            "Authorization": "Basic MmNjYzE2NzY5YjFhYWMwMmY5MDJjNDY3NzM4NTE2NjU6MGM1NWZjMzFjZTU0NTQ4NGY5M2QyMzM3ZDhhNjJiNzQ="
        },
        data={
            "fromDate": start_of_week.strftime("%Y-%m-%d"),
            "endDate": current_datetime.strftime("%Y-%m-%d"),
            "limit": 1000,
        },
    )
    if not json_response["success"]:
        return False
    await Lead.all().delete()
    for row in json_response["response"]["data"]:
        new_lead = Lead(**row)
        await new_lead.save()

    return True


async def fetch_leads_data():
    leads = await Lead.all()
    for lead in leads:
        response_data = await fetch_data(
            "post",
            "https://api.leadspedia.com/core/v2/leads/getLeadData.do",
            headers={
                "Authorization": "Basic MmNjYzE2NzY5YjFhYWMwMmY5MDJjNDY3NzM4NTE2NjU6MGM1NWZjMzFjZTU0NTQ4NGY5M2QyMzM3ZDhhNjJiNzQ="
            },
            data={"leadID": lead.leadID},
        )

        if not response_data.get("success", None):
            continue

        await LeadData.filter(lead=lead).delete()
        for type in response_data["data"].keys():
            (uniqueName, fieldLabel, value) = response_data["data"][type].values()
            lead_data = LeadData(
                lead=lead,
                uniqueName=uniqueName,
                fieldLabel=fieldLabel,
                value=value,
                leadID=lead.leadID,
            )
            await lead_data.save()
    return True


async def fetch_advertisers_data():
    response = await fetch_data(
        "get",
        "https://api.leadspedia.com/core/v2/advertisers/getAll.do",
        headers={
            "Authorization": "Basic MmNjYzE2NzY5YjFhYWMwMmY5MDJjNDY3NzM4NTE2NjU6MGM1NWZjMzFjZTU0NTQ4NGY5M2QyMzM3ZDhhNjJiNzQ="
        },
    )

    if not response["success"]:
        return False

    await Advertiser.all().delete()
    for datum in response["response"]["data"]:
        await Advertiser(**datum).save()

    return True


async def fetch_affiliates_data():
    response = await fetch_data(
        "get",
        "https://api.leadspedia.com/core/v2/affiliates/getAll.do",
        headers={
            "Authorization": "Basic MmNjYzE2NzY5YjFhYWMwMmY5MDJjNDY3NzM4NTE2NjU6MGM1NWZjMzFjZTU0NTQ4NGY5M2QyMzM3ZDhhNjJiNzQ="
        },
    )

    if not response["success"]:
        return False

    await Affiliate.all().delete()
    for datum in response["response"]["data"]:
        await Affiliate(**datum).save()

    return True


async def fetch_compaigns_data():
    response = await fetch_data(
        "get",
        "https://api.leadspedia.com/core/v2/campaigns/getAll.do",
        headers={
            "Authorization": "Basic MmNjYzE2NzY5YjFhYWMwMmY5MDJjNDY3NzM4NTE2NjU6MGM1NWZjMzFjZTU0NTQ4NGY5M2QyMzM3ZDhhNjJiNzQ="
        },
    )

    if not response["success"]:
        return False

    await Compaign.all().delete()
    for datum in response["response"]["data"]:
        await Compaign(**datum).save()

    return True


async def fetch_contacts_data():
    response = await fetch_data(
        "get",
        "https://api.leadspedia.com/core/v2/affiliatesContacts/getAll.do",
        headers={
            "Authorization": "Basic MmNjYzE2NzY5YjFhYWMwMmY5MDJjNDY3NzM4NTE2NjU6MGM1NWZjMzFjZTU0NTQ4NGY5M2QyMzM3ZDhhNjJiNzQ="
        },
    )

    if not response["success"]:
        return False

    await Contact.all().delete()
    for datum in response["response"]["data"]:
        await Contact(**datum).save()

    return True


async def fetch_offers_data():
    response = await fetch_data(
        "get",
        "https://api.leadspedia.com/core/v2/offers/getAll.do",
        headers={
            "Authorization": "Basic MmNjYzE2NzY5YjFhYWMwMmY5MDJjNDY3NzM4NTE2NjU6MGM1NWZjMzFjZTU0NTQ4NGY5M2QyMzM3ZDhhNjJiNzQ="
        },
    )

    if not response["success"]:
        return False

    await Offer.all().delete()
    for datum in response["response"]["data"]:
        await Offer(**datum).save()

    return True


async def fetch_verticles_data():
    response = await fetch_data(
        "get",
        "https://api.leadspedia.com/core/v2/verticals/getAll.do",
        headers={
            "Authorization": "Basic MmNjYzE2NzY5YjFhYWMwMmY5MDJjNDY3NzM4NTE2NjU6MGM1NWZjMzFjZTU0NTQ4NGY5M2QyMzM3ZDhhNjJiNzQ="
        },
    )

    if not response["success"]:
        return False

    await Verticle.all().delete()
    for datum in response["response"]["data"]:
        await Verticle(**datum).save()

    return True


async def fetch_all():
    print("Fetching data from 8 urls in parallel. Please wait...")
    responses1 = await asyncio.gather(
        fetch_leads(),
        fetch_advertisers_data(),
        fetch_affiliates_data(),
        fetch_compaigns_data(),
        fetch_contacts_data(),
        fetch_offers_data(),
        fetch_verticles_data(),
    )
    print(f"Getting response2 data..................")
    response2 = await fetch_leads_data()
    successes = 0
    errors = 0

    print([*responses1, response2])
    for response, model_name in zip(
        [*responses1, response2],
        [
            "Lead",
            "Advertiser",
            "Affiliate",
            "Compaign",
            "Contact",
            "Offer",
            "Verticle",
            "LeadData",
        ],
    ):
        if response:
            successes += 1
            await DataUpdateLog.create(model_name=model_name, status="success")
        else:
            errors += 1
            await DataUpdateLog.create(
                model_name=model_name,
                status="failed",
                error_message="Data fetch failed",
            )

    print(
        f"{successes} url(s) were fetched successfully. Unable to completely fetch {errors} url(s)"
    )
    return {"successes": successes, "errors": errors}


async def fetch_yearly_data():
    print("Fetching yearly data from 8 urls in parallel. Please wait...")
    responses1 = await asyncio.gather(
        fetch_yearly_leads(),
        fetch_advertisers_data(),
        fetch_affiliates_data(),
        fetch_compaigns_data(),
        fetch_contacts_data(),
        fetch_offers_data(),
        fetch_verticles_data(),
    )
    print(f"Getting response2 data..................")
    response2 = await fetch_leads_data()
    successes = 0
    errors = 0

    print([*responses1, response2])
    for response, model_name in zip(
        [*responses1, response2],
        [
            "Lead",
            "Advertiser",
            "Affiliate",
            "Compaign",
            "Contact",
            "Offer",
            "Verticle",
            "LeadData",
        ],
    ):
        if response:
            successes += 1
            await DataUpdateLog.create(
                model_name=model_name,
                status="success",
            )
        else:
            errors += 1
            await DataUpdateLog.create(
                model_name=model_name,
                status="failed",
                error_message="Data fetch failed",
            )

    print(
        f"{successes} url(s) were fetched successfully. Unable to completely fetch {errors} url(s)"
    )
    return {"successes": successes, "errors": errors}


async def fetch_weekly_data():
    print("Fetching weekly data from 8 urls in parallel. Please wait...")
    responses1 = await asyncio.gather(
        fetch_weekly_leads(),
        # fetch_advertisers_data(),
        # fetch_affiliates_data(),
        # fetch_compaigns_data(),
        # fetch_contacts_data(),
        # fetch_offers_data(),
        # fetch_verticles_data(),
    )
    print(f"Getting response2 data..................")
    # response2 = await fetch_leads_data()
    successes = 0
    errors = 0

    print([*responses1])
    for response, model_name in zip(
        [*responses1],
        [
            "Lead",
            "Advertiser",
            "Affiliate",
            "Compaign",
            "Contact",
            "Offer",
            "Verticle",
            "LeadData",
        ],
    ):
        if response:
            successes += 1
            await DataUpdateLog.create(
                model_name=model_name,
                status="success",
            )
        else:
            errors += 1
            await DataUpdateLog.create(
                model_name=model_name,
                status="failed",
                error_message="Data fetch failed",
            )

    print(
        f"{successes} url(s) were fetched successfully. Unable to completely fetch {errors} url(s)"
    )
    return {"successes": successes, "errors": errors}


async def get_data():
    data = {}
    current_datetime = datetime.datetime.now()
    current_day = current_datetime.strftime("%A")
    if (
        current_day == "Sunday"
        and current_datetime.hour == 0
        and current_datetime.minute == 0
    ):
        data = {
            "fromDate": (current_datetime - datetime.timedelta(days=365)).strftime(
                "%Y-%m-%d"
            ),
            "endDate": current_datetime.strftime("%Y-%m-%d"),
            "limit": 1000,
        }
    else:
        from_date_setting = await Setting.filter(key="from_date").first()
        end_date_setting = await Setting.filter(key="end_date").first()

        if (
            from_date_setting is None
            or end_date_setting is None
            or not from_date_setting.value
            or not end_date_setting.value
        ):
            return {
                "success": False,
                "message": "Valid value for fromDate and endDate is required (YYYY-MM-DD)",
            }

        data = {
            "fromDate": from_date_setting.value,
            "endDate": end_date_setting.value,
            "limit": 1000,
        }

    return data


# ___________________________________________________________________
# async def fetch_all():
#     print("Fetching data from 8 urls in parallel. Please wait...")

#     responses1 = await asyncio.gather(
#         fetch_leads(),
#         fetch_advertisers_data(),
#         fetch_affiliates_data(),
#         fetch_compaigns_data(),
#         fetch_contacts_data(),
#         fetch_offers_data(),
#         fetch_verticles_data()
#     )
#     response2 = await fetch_leads_data()

#     successes = 0
#     errors = 0

#     print([*responses1, response2])
#     for response in [*responses1, response2]:
#         if response:
#             successes += 1
#         else:
#             errors += 1
#     print(f"{successes} url(s) were fetched successfully. Unable to completely fetch {errors} url(s)")
#     return { "successes": successes, "errors": errors }
