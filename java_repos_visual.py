import requests
from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store data
url = 'https://api.github.com/search/repositories?q=language:java&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Request Status: {r.status_code}')

# Organize the data
all_data = r.json()
item_dicts = all_data["items"]
stars, labels, links = [], [], []
for item_dict in item_dicts:
    name = item_dict["name"]

    stars.append(item_dict["stargazers_count"])

    label = item_dict["description"]
    owner = item_dict["owner"]["login"]
    labels.append(f'Owner: {owner}<br>Description: {label}')

    link = item_dict["html_url"]
    links.append(f"<a href='{link}'>{name}</a>")

data = {
    'type': 'bar',
    'x': links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}

layout = {
    'title': 'Most-Starred Java Projects On Github',
    'xaxis': {'title': 'Repository',
              'titlefont': {'size': 24},
              'tickfont': {'size': 14},
              },
    'yaxis': {'title': 'Stars',
              'titlefont': {'size': 24},
              'tickfont': {'size': 14},
              }
}

fig = {'data': data, 'layout': layout}

offline.plot(fig, filename='java_repos.html')
