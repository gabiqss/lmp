import requests
import json

def consult_cnpj(cnpj):
    url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
    querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX","cnpj":"06990590000123","plugin":"RF"}
    response = requests.request('GET', url, params=querystring)

    resp = json.loads(response.text)

    return resp


def formfield(self, **kwargs):
    kwargs['widget'] = forms.Textarea(attrs={'class': 'textarea'})
    #return super().formfield(**kwargs)



    