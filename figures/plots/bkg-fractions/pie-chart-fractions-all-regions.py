import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

# Props change to this:
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/horizontal_barchart_distribution.html

glabels = {
    "otherVV": "Other $VV$($V$)",
    "Misid": "Mis-Id",
    "Zjets": "$Z/\gamma*$",
    "WW": "$WW$",
    "WWStrong": "$WW$ (Strong)",
    "EWWW": "$WW$ (EW)",
    "Top": "$t\\bar{t}$/$Wt$",
    "vbf": "$H_{\mathrm{VBF}}$",
    "ggf": "$H_{\mathrm{ggF}}$"}
# "Mis-Id"

gcolors = {
    "Misid": "#3DFDFF",  # sns.color_palette("Paired")[9], # vgamma purple
    # "s_otherVV_step": "#CAB2D6",# sns.color_palette("Paired")[8], # other VV light purple
    # sns.color_palette("Paired")[8], # other VV light purple
    "otherVV": "#6A3D9A",
    "Zjets": "#33A02C",  # sns.color_palette("Paired")[3], # Zjets green
    "WW": "#2578B4",  # sns.color_palette("Paired")[1],  # WW blue
    "WWStrong": "#2578B4",  # sns.color_palette("Paired")[1],  # WW blue
    "EWWW": "#A5CEE3",  # sns.color_palette("Paired")[0], # EW WW light blue
    # "Top": "#FCFF99",# sns.color_palette("Paired")[10], # singletop light yellow
    "Top": "#FBD930",  # sns.color_palette("Set2")[5], # ttbar yellow
    "vbf": "#FA7F00",  # sns.color_palette("Paired")[7]] # VBF orange
    "ggf": "#E31E1C"  # sns.color_palette("Paired")[5], # ggF red
}

# EW WW in VBF region is 2.3467216
values = {"ggF0jet": {
    #"ggf": 2100,
    "vbf": 23,
    "WW": 9700,
    "Top": 2200,
    # "EWWW": 0,
    "Zjets": 140,
    # "s_Vgamma_step": 0.5875710478841825,
    "otherVV": 1400,
    "Misid": 1200
},
    "ggF1jet": {
   # "ggf": 1100,
    "vbf": 103,
    "WW": 3500,
    "Top": 5300,
    # "EWWW": 0,
    "Zjets": 280,
    # "s_Vgamma_step": 0.5875710478841825,
    "otherVV": 840,
    "Misid": 720
},
    "ggF2jet": {
    #"ggf": 440,
    "vbf": 46,
    "WW": 1500,
    "Top": 6100,
    # "EWWW": 0,
    "Zjets": 930,
    # "s_Vgamma_step": 0.5875710478841825,
    "otherVV": 470,
    "Misid": 470
},
    "vbf": {
    "ggf": 2.6,
    #"vbf": 28.8,
    "WWStrong": 2.3,
    "EWWW": 2.3,
    "Top": 2.6,
    # "EWWW": 0,
    "Zjets": 0.6,
    # "s_Vgamma_step": 0.5875710478841825,
    "otherVV": 0.6,
    "Misid": 1.7
}
}

# , "Total": 45.0865771941845}

def plot_pie_chart(values, key):
    global gcolors
    global glabels

    chosen = values[key]
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    print(chosen.keys())
    colors = [gcolors[n] for n in chosen.keys()]
    labels = [glabels[n] for n in chosen.keys()]
    sizes = chosen.values()
    # only "explode" the 2nd slice (i.e. 'Hogs')

    # ggF is 3
    #explode = (0, 0, 0, 0, 0.0, 0, 0, 0)
    #explode = (0.2, 0.05, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2)

    def func(pct, allvals, key):
        absolute = np.round(pct/100.*np.sum(allvals), 1)
        if "vbf" in key:
            return "{:.1f}%\n({:.1f})".format(pct, absolute)
        else:
            return "{:.1f}%\n({:.0f})".format(pct, absolute)

    fig1, ax1 = plt.subplots()
    patches, texts, autotexts = ax1.pie(sizes, labels=labels,  # autopct='%1.1f%%',
                                        autopct=lambda pct: func(pct, sizes, key),
                                        shadow=False, startangle=90, colors=colors, labeldistance=1.1, pctdistance=0.73)
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.axis('equal')

    plt.setp(texts, size=14)
    plt.setp(autotexts, size=10, weight="bold")
    plt.setp(patches, linewidth=0)

    autotexts[2].set_fontsize(8)  # MisId
    # autotexts[3].set_color('white')  # WW
    # autotexts[6].set_color('white')  # Zjets
    # autotexts[1].set_color('white')  # ggF

    # texts[6].set_position((texts[6].get_position()[0]-0.07,
    #                       texts[6].get_position()[1]+0.05))  # Zjets
    # autotexts[5].set_text('')  # Wt
    # texts[5].set_position((texts[5].get_position()[0]-0.07,
    #                       texts[5].get_position()[1]+0.01))  # Wt

    # # autotexts[0].set_text('') # Vgamma
    # # autotexts[8].set_text('')  # other VV
    # # texts[8].set_position((texts[8].get_position()[0]-0.14,
    # #                       texts[8].get_position()[1]+0.06))  # other VV
    # texts[7].set_position((texts[7].get_position()[0]-0.01,
    #                       texts[7].get_position()[1]-0.02))  # ttbar

    # plt.show()
    plt.savefig('pie-chart-fractions-'+key+'.pdf')
    plt.close()

plot_pie_chart(values, "ggF0jet")
plot_pie_chart(values, "ggF1jet")
plot_pie_chart(values, "ggF2jet")
plot_pie_chart(values, "vbf")
