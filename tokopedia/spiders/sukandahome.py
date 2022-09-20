# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.request.json_request import JsonRequest
from pprint import pprint
from scrapy import Request
import requests
import json

class SukandahomeSpider(scrapy.Spider):
    name = 'sukandahome'
    allowed_domains = ['tokopedia.com']
    start_urls = ['https://www.tokopedia.com/sukandahome/product']
    
    def parse(self, response):
        url = 'https://gql.tokopedia.com/graphql/ShopProducts'

        headers = {
            "authority": "gql.tokopedia.com",
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "origin": "https://www.tokopedia.com",
            "referer": "https://www.tokopedia.com/sukandahome/product",
            "sec-ch-ua": "\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
            "x-device": "default_v3",
            "x-source": "tokopedia-lite",
            "x-tkpd-lite-service": "zeus",
            "x-version": "cc55714"
        }

        cookies = {
            "_UUID_NONLOGIN_": "e0e797215bf27f8e6914cfda1fe2a7f9",
            "_UUID_NONLOGIN_.sig": "wq8575LN4w0EsDCkYwWNdG-erJc",
            "_gcl_au": "1.1.416165113.1662396502",
            "_gid": "GA1.2.1140986955.1662396502",
            "_SID_Tokopedia_": "ssG1EQQasWyrtDTgN2P9ROcw3qx76L6TQn24xyLqv_HRd89j3BF41OGRkLNf_DWr8__N6b8LZbnuzu-aHTQQiz6YvcsieuW0VNEb1C2yenzWphE1n49-MAgCB7CP46HS",
            "DID": "24e1b8f1513f9487e9ed605beee478491866e041b051d6d598f0bc010c6609aa6e249e04eb0f1d27d2c4bcb7953a0520",
            "DID_JS": "MjRlMWI4ZjE1MTNmOTQ4N2U5ZWQ2MDViZWVlNDc4NDkxODY2ZTA0MWIwNTFkNmQ1OThmMGJjMDEwYzY2MDlhYTZlMjQ5ZTA0ZWIwZjFkMjdkMmM0YmNiNzk1M2EwNTIw47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=",
            "_UUID_CAS_": "60cb2f5c-60fe-46ef-afc8-8e26888878c6",
            "_CASE_": "257c3a173a7c646c6c696a727c3f173a7c646e727c323c327c647c143f353f2c2a3f7e0e2b2d3f2a7c727c3d173a7c646f6968727c323130397c647c7c727c323f2a7c647c7c727c2e1d317c647c7c727c29173a7c646f6c6c6f6e6d696b727c2d173a7c646f6f6b6d6e6b696d727c2d0a272e3b7c647c6c367c727c29362d7c647c0525027c293f2c3b36312b2d3b01373a027c646f6c6c6f6e6d696b72027c2d3b2c28373d3b012a272e3b027c64027c6c36027c72027c01012a272e3b303f333b027c64027c093f2c3b36312b2d3b2d027c237225027c293f2c3b36312b2d3b01373a027c646e72027c2d3b2c28373d3b012a272e3b027c64027c6f6b33027c72027c01012a272e3b303f333b027c64027c093f2c3b36312b2d3b2d027c23037c727c320b2e3a7c647c6c6e6c6c736e67736e6b0a6c6d646a66646c6d756e69646e6e7c23",
            "__auc": "f077fff71830e8da5c476bdfe0f",
            "_fbp": "fb.1.1662431995606.1702421209",
            "__asc": "68043e30183112f0b3a4bafbb87",
            "_abck": "4E0B9D3679E5192338C6AFF1404E57FF~0~YAAQZsMmFy1OyQ+DAQAATncxEQj+2CPQHIfHS1uZlBRzCx1nPBzAvnhIJPPdfC6N3gD8j8jqjRVqWEcx7Dc4X7B8+aTkmD7zPlN8taSbv7vq1HdRY+OlvCQhIx6QpOaZ50oLTOQtMcXXlXrSZ9CCx1m4k7se2JjBvu2zj4AR/Vmw5+rziLnVCv27AwiE3okcT8I+dfJKIBK4piEJpV9tgFstPuSluMVEHd9sqX6laplASinFBCoIFud87kzV1EFWi2tBpq9v/WTfoaruBgSSDW9N06cPSWWfTCkkEI27a8av2XDTsOqqAVTVzRFEKhFEgSGg043muht7U7QDjygOh3GcFL2w0uiwZr3dQ0NRhdXRQ/Rh2ZytjForBTkldgS+nbGsqEv8of9n1z8Alf1I9XkuCpM79FQn~-1~-1~-1",
            "bm_sz": "9BB50EC95AAD51C5A7B7485A5CCD2B2E~YAAQbOwZuCJ8IgCDAQAAoQ9JEREhXgHyvNFqFP8Lk33McmdeYJPIR4smeQjELNSQUKQn9J01f4hksooviKeRawulrSNhIqSef+ljAtqbp45kC0uySc52cowx66hq2qgFdzsZjgWIhXZ87gpbjiaCkwytmXn0CyfrKNSLbHvPM2lPMLA4pHFkl/Gh+vYo2C4MqAUaILAtBwFRd/8B7WZvg9CKPKzk4WFIAXer92NHtxXw0020WYqj0QqXfSRFUJuESxTtCIAOGIkdOb7Gfu59KXsCaWJSJdO9+DYPpNHMkRkwBTDoGSfW5VabSRn5xClNORLpK0eZfl6M1TskkzI=~3294265~4338740",
            "_dc_gtm_UA-126956641-6": "1",
            "_ga_70947XW48P": "GS1.1.1662440574.6.1.1662442345.60.0.0",
            "_ga": "GA1.2.931480074.1662396502",
            "_dc_gtm_UA-9801603-1": "1"
        }

        query = """query ShopProducts($sid: String, $page: Int, $perPage: Int, $keyword: String, $etalaseId: String, $sort: Int, $user_districtId: String, $user_cityId: String, $user_lat: String, $user_long: String) {  GetShopProduct(shopID: $sid, filter: {page: $page, perPage: $perPage, fkeyword: $keyword, fmenu: $etalaseId, sort: $sort, user_districtId: $user_districtId, user_cityId: $user_cityId, user_lat: $user_lat, user_long: $user_long}) {    status    errors    links {      prev      next      __typename    }    data {      name      product_url      product_id      price {        text_idr        __typename      }      primary_image {        original        thumbnail        resize300        __typename      }      flags {        isSold        isPreorder        isWholesale        isWishlist        __typename      }      campaign {        discounted_percentage        original_price_fmt        start_date        end_date        __typename      }      label {        color_hex        content        __typename      }      label_groups {        position        title        type        url        __typename      }      badge {        title        image_url        __typename      }      stats {        reviewCount        rating        __typename      }      category {        id        __typename      }      __typename    }    __typename  }}
        """

        json_data = {
            'query': query,
            'variables': {"sid":"8656196","page":1,"perPage":80,"etalaseId":"etalase","sort":1,"user_districtId":"2274","user_cityId":"176","user_lat":"","user_long":""},
            'operationName': 'ShopProducts',
        }

        request = requests.post(
            url=url,
            headers=headers,
            data=json_data
            # cookies=cookies,
        )
        print("Donal")
        pprint(request.json())
        # fetch(request)