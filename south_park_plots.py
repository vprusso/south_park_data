import plotly.offline as offline
import plotly.graph_objs as go

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def plot_swear_count_season_frequency():

    ass = [152, 207, 269, 189, 147, 164, 136, 123, 99, 125, 122, 78, 96, 61, 117, 110, 48, 62]
    damn = [100, 115, 104, 79, 77, 79, 64, 54, 53, 50, 38, 45, 37, 32, 28, 26, 17, 23] # damn or dammit
    fuck = [19, 48, 29, 14, 15, 29, 29, 43, 15, 18, 32, 53, 106, 162, 133, 100, 71, 85]
    shit = [5, 21, 10, 7, 168, 25, 16, 7, 7, 4, 35, 10, 18, 21, 116, 30, 30, 44]

    trace1 = go.Scatter(
        x=['S-1', 'S-2', 'S-3', 'S-4', 'S-5', 'S-6', 'S-7', 'S-8', 'S-9', 'S-10', 'S-11', 'S-12', 'S-13', 'S-14', 'S-15', 'S-16', 'S-17', 'S-18'],
        y=ass,
        mode='lines+markers',
        name="'Ass'",
        hoverinfo='name',
        line=dict(
            shape='linear'
        )
    )
    trace2 = go.Scatter(
        x=['S-1', 'S-2', 'S-3', 'S-4', 'S-5', 'S-6', 'S-7', 'S-8', 'S-9', 'S-10', 'S-11', 'S-12', 'S-13', 'S-14', 'S-15', 'S-16', 'S-17', 'S-18'],
        y=damn,
        mode='lines+markers',
        name="'Damn/Dammit'",
        hoverinfo='name',
        line=dict(
            shape='linear'
        )
    )
    trace3 = go.Scatter(
        x=['S-1', 'S-2', 'S-3', 'S-4', 'S-5', 'S-6', 'S-7', 'S-8', 'S-9', 'S-10', 'S-11', 'S-12', 'S-13', 'S-14', 'S-15', 'S-16', 'S-17', 'S-18'],
        y=fuck,
        mode='lines+markers',
        name="'Fuck'",
        hoverinfo='name',
        line=dict(
            shape='linear'
        )
    )
    trace4 = go.Scatter(
        x=['S-1', 'S-2', 'S-3', 'S-4', 'S-5', 'S-6', 'S-7', 'S-8', 'S-9', 'S-10', 'S-11', 'S-12', 'S-13', 'S-14', 'S-15', 'S-16', 'S-17', 'S-18'],
        y=shit,
        mode='lines+markers',
        name="'Shit'",
        hoverinfo='name',
        line=dict(
            shape='linear'
        )
    )
    data = [trace1, trace2, trace3, trace4]
    layout = dict(
        title="Occurrence of Swear Word by Season",
        xaxis = dict(title = 'South Park Season'),
        yaxis = dict(title = 'Swear Word Frequency'),        
        legend=dict(
            x=1,
            y=0.5,
            font=dict(
                size=16
            )
        ),
    )    
    fig = go.Figure(data=data, layout=layout)
    offline.plot(fig)


def plot_swear_words_per_character():
    fig = {
        'data': [
            {
                'labels': ['Cartman', 'Stan', 'Kyle', 'Kenny'],
                'values': [501, 220, 285, 17],
                'type': 'pie',
                'name': 'Ass',
                'marker': {'colors': ['rgb(90,192,214)',
                                      'rgb(81,97,172)',
                                      'rgb(108,192,106)',
                                      'rgb(244,115,32)']},
                'domain': {'x': [0, .48],
                           'y': [0, .49]},
                'hoverinfo':'label+percent+name'
            },
            {
                'labels': ['Cartman', 'Stan', 'Kyle', 'Kenny'],
                'values': [311, 111, 122, 17],
                'marker': {'colors': ['rgb(90,192,214)',
                                      'rgb(81,97,172)',
                                      'rgb(108,192,106)',
                                      'rgb(244,115,32)']},
                'type': 'pie',
                'name': 'Damn/Dammit',
                'domain': {'x': [.52, 1],
                           'y': [0, .49]},
                'hoverinfo':'label+percent+name'

            },
            {
                'labels': ['Cartman', 'Stan', 'Kyle', 'Kenny'],
                'values': [295, 56, 71, 83],
                'marker': {'colors': ['rgb(90,192,214)',
                                      'rgb(81,97,172)',
                                      'rgb(108,192,106)',
                                      'rgb(244,115,32)']},
                'type': 'pie',
                'name': 'Fuck',
                'domain': {'x': [0, .48],
                           'y': [.51, 1]},
                'hoverinfo':'label+percent+name'
            },
            {
                'labels': ['Cartman', 'Stan', 'Kyle', 'Kenny'],
                'values': [82, 62, 40, 11],
                'marker': {'colors': ['rgb(90,192,214)',
                                      'rgb(81,97,172)',
                                      'rgb(108,192,106)',
                                      'rgb(244,115,32)']},
                'type': 'pie',
                'name':'Shit',
                'domain': {'x': [.52, 1],
                           'y': [.51, 1]},
                'hoverinfo':'label+percent+name'
            }
        ],
        'layout': {'title': 'Proportion of Swear Words Spoken by Per Character'}
    }
    offline.plot(fig)
    

def plot_total_lines_of_dialog():
    x = ['Cartman', 'Stan', 'Kyle', 'Kenny']
    y = [9911, 7900, 7419, 923]

    trace0 = go.Bar(
                x=["Cartman"],y=[9911],
                name="Cartman",
                marker=dict(
                    color='rgb(90,192,214)',
                    line=dict(
                        color='rgb(8,48,107)',
                        width=1.5),
                ),
                opacity=0.8
            )

    trace1 = go.Bar(
                x=["Stan"],y=[7900],
                name="Stan",
                marker=dict(
                    color='rgb(81,97,172)',
                    line=dict(
                        color='rgb(8,48,107)',
                        width=1.5),
                ),
                opacity=0.8
            )

    trace2 = go.Bar(
                x=["Kyle"],y=[7419],
                name="Kyle",
                marker=dict(
                    color='rgb(108,192,106)',
                    line=dict(
                        color='rgb(8,48,107)',
                        width=1.5),
                ),
                opacity=0.8
            )

    trace3 = go.Bar(
                x=["Kenny"],y=[923],
                name="Kenny",
                marker=dict(
                    color='rgb(244,115,32)',
                    line=dict(
                        color='rgb(8,48,107)',
                        width=1.5),
                ),
                opacity=0.8
            )

    layout = go.Layout(
        title='Total Lines of Dialog Per Character',
        xaxis=dict(
            title="South Park Character",
        ),
        yaxis=dict(
            title='Total Lines of Dialog',
        ),    
        annotations=[
            dict(x=xi,y=yi,
                 text=str(yi),
                 xanchor='center',
                 yanchor='bottom',
                 showarrow=False,
            ) for xi, yi in zip(x, y)]
    )

    data = [trace0, trace1, trace2, trace3]

    fig = go.Figure(data=data, layout=layout)
    offline.plot(fig)    


def determine_most_frequent_non_stop_words(dialog_file):

    f = codecs.open(dialog_file, 'r', "utf-8-sig")
    dialog = f.read()

    stop_words = set(stopwords.words("english"))
    filler_words = ['oh', 'get', 'yeah', 'na', 'well', 'know', 'right', 'like', 'go', 'got', \
    'come', 'gon', 'let', 'see', 'us', 'hey', 'okay', 'uh', 'ca', 'one', 'look', 'little', \
    'really', 'want', 'yes', 'make', 'good', 'take', 'need', 'would', 'could', 'say', 'way',\
     'sure', 'tell', 'think', 'people', 'back', 'going', 'alright', 'wan', 'wait', 'everyone',\
     'huh', 'give', 'new', 'never', 'thing', 'boy', 'hello', 'said', 'great', 'put', 'even',\
     'maybe', 'better', 'something', 'ta', 'must', 'still', 'ever', 'made']
    dialog = dialog.lower()
    words = word_tokenize(dialog)

    filtered_dialog = [w for w in words if not w in stop_words and not w in filler_words and w.isalpha()]
    
    text = nltk.Text(filtered_dialog)
    fdist = nltk.FreqDist(text)
    vocab = fdist.keys()
    fdist.plot(50, cumulative=True)


# Uncomment functions to plot figures:
# plot_swear_count_season_frequency()
# plot_swear_words_per_character()
# plot_total_lines_of_dialog()
# determine_most_frequent_non_stop_words("sp_season_dialog.csv")