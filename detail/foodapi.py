from urllib.request import Request, urlopen
from django.http import HttpResponse
import json
import urllib

def read_data():
    apikey = '807d295ff3754e9ba9d9'
    startRow = 1
    endRow = 150
    url = 'http://openapi.foodsafetykorea.go.kr/api/'+apikey+'/I2790/json/'+str(startRow)+'/'+str(endRow)

    data = urllib.request.urlopen(url).read()
    # json_object = json.dumps(data)
    output = json.loads(data)
    # print (output)
    return output

    # ingredientDDF = pd.DataFrame()
    # ingredientDDF = ingredientDDF.append(
    #     {"NUM":"",
    #     "GROUP_NAME":"","DESC_KOR":"","MAKER_NAME":"",
    #     "NUTR_CONT1":"","NUTR_CONT2":"","NUTR_CONT3":"","NUTR_CONT4":"",
    #     "NUTR_CONT5":"","NUTR_CONT6":"","NUTR_CONT7":"","NUTR_CONT8":"","NUTR_CONT9":""
    #     },
    #     ignore_index=True
    # )
    # total = output["I2790"]["total_count"]
    # num = len(output["I2790"]["row"])

    # for i in range(0,num):
    #     ingredientDDF.ix[i,"NUTR_CONT1"]=output["I2790"]["row"][i]["NUTR_CONT1"]
    #     ingredientDDF.ix[i,"NUTR_CONT2"]=output["I2790"]["row"][i]["NUTR_CONT2"]
    #     ingredientDDF.ix[i,"NUTR_CONT3"]=output["I2790"]["row"][i]["NUTR_CONT3"]
    #     ingredientDDF.ix[i,"NUTR_CONT4"]=output["I2790"]["row"][i]["NUTR_CONT4"]
    #     ingredientDDF.ix[i,"NUTR_CONT5"]=output["I2790"]["row"][i]["NUTR_CONT5"]
    #     ingredientDDF.ix[i,"NUTR_CONT6"]=output["I2790"]["row"][i]["NUTR_CONT6"]
    #     ingredientDDF.ix[i,"NUTR_CONT7"]=output["I2790"]["row"][i]["NUTR_CONT7"]
    #     ingredientDDF.ix[i,"NUTR_CONT8"]=output["I2790"]["row"][i]["NUTR_CONT8"]
    #     ingredientDDF.ix[i,"NUTR_CONT9"]=output["I2790"]["row"][i]["NUTR_CONT9"]
    #     ingredientDDF.ix[i,"NUM"]=output["I2790"]["row"][i]["NUM"]
    #     ingredientDDF.ix[i,"DESC_KOR"]=output["I2790"]["row"][i]["DESC_KOR"]
    #     ingredientDDF.ix[i,"GROUP_NAME"]=output["I2790"]["row"][i]["GROUP_NAME"]
    #     ingredientDDF.ix[i,"MAKER_NAME"]=output["I2790"]["row"][i]["MAKER_NAME"]
    # ingredientDDF.to_csv("filename.csv",header=True,index=False,encoding='utf-8')
    # time.sleep(60)

    # print(ingredientDDF)

        # {"NUM":"","FOOD_CD":"","SAMPLING_REGION_NAME":"","SAMPLING_MONTH_NAME":"","SAMPLING_REGION_CD":"",
        # "SAMPLING_MONTH_CD":"","GROUP_NAME":"","DESC_KOR":"","RESEARCH_YEAR":"","MAKER_NAME":"",
        # "SUB_REF_NAME":"","SERVING_SIZE":"","NUTR_CONT1":"","NUTR_CONT2":"","NUTR_CONT3":"",
        # "NUTR_CONT4":"","NUTR_CONT5":"","NUTR_CONT6":"","NUTR_CONT7":"","NUTR_CONT8":"","NUTR_CONT9":""
        # },

# read_data()