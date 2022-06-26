from ctypes import alignment
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

# RUN with python3

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
    "VBF": "$H_{\mathrm{VBF}}$",
    "ggF": "$H_{\mathrm{ggF}}$"}
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
    "VBF": "#FA7F00",  # sns.color_palette("Paired")[7]] # VBF orange
    "ggF": "#E31E1C"  # sns.color_palette("Paired")[5], # ggF red
}

category_names = ['VBF', 'ggF', 'WWStrong', 'EWWW',
                  'Top', 'Zjets', 'otherVV', 'Misid']
results = {"ggF N$_{\mathrm{jet}} =$ 0 SR": [21, 0, 9486, 2.4, 2050, 93, 1028, 1263], 
"ggF N$_{\mathrm{jet}} =$ 1 SR": [103, 0, 4168, 16, 5112, 272, 721, 797], 
"ggF N$_{\mathrm{jet}} \geq$ 2 SR": [56, 0, 1973, 30, 6033, 1036, 503, 513], 
#"VBF N$_{\mathrm{jet}} \geq$ 2 SR": [0, 81, 160, 28.5, 336, 138, 56, 52], 
"VBF N$_{\mathrm{jet}} \geq$ 2 SR,    \nDNN output > 0.87": [0, 2.8, 2.12, 2.5, 3.06, 0.72, 0.68, 1.81], 
}

integrals = [sum(v) for v in results.values()]
print(integrals)
for k in results.keys():
    results[k] = list(map(lambda x: x / sum(results[k]) * 100, results[k]))
print(results)

# EW WW in VBF region is 2.3467216
values = {"ggF0jet": {
    #"ggf": 2100,
    "vbf": 23,
    "ggf": 2100,
    "WW": 9700,
    "Top": 2200,
    # "EWWW": 0,
    "Zjets": 140,
    # "s_Vgamma_step": 0.5875710478841825,
    "otherVV": 1400,
    "Misid": 1200
},
    "ggF1jet": {
    "vbf": 103,
    "ggf": 1100,
    "WW": 3500,
    "Top": 5300,
    # "EWWW": 0,
    "Zjets": 280,
    # "s_Vgamma_step": 0.5875710478841825,
    "otherVV": 840,
    "Misid": 720
},
    "ggF2jet": {
    "vbf": 46,
    "ggf": 440,
    "WW": 1500,
    "Top": 6100,
    # "EWWW": 0,
    "Zjets": 930,
    # "s_Vgamma_step": 0.5875710478841825,
    "otherVV": 470,
    "Misid": 470
},
    "vbf": {
    "vbf": 28.8,
    "ggf": 2.6,
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

#labels = [glabels[n] for n in category_names]
labels = list(results.keys())
data = np.array(list(results.values()))
data_cum = data.cumsum(axis=1)
category_colors = [gcolors[n] for n in category_names]

fig, ax = plt.subplots(figsize=(10, 4))
ax.invert_yaxis()
ax.xaxis.set_visible(False)
ax.set_xlim(0, np.sum(data, axis=1).max())

for i, (colname, color) in enumerate(zip(category_names, category_colors)):
    widths = data[:, i]
    starts = data_cum[:, i] - widths
    rects = ax.barh(labels, widths, left=starts, height=0.66, 
                    label=glabels[colname], color=color)

    # r, g, b, _ = color
    # text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
    if colname == "ggF" or colname == "WWStrong":
        text_color='#F0F0F0'
    else:   
        text_color = '#0F0F0F'
    #percentages = ["{:.0f} \n{:.1f}%)".format(v*i/100, v) if v > 11 else "" for v,i in zip(rects.datavalues, integrals)]
    percentages = ["{:.1f}%".format(v) if v > 10 else "" for v,i in zip(rects.datavalues, integrals)]
    ax.bar_label(rects, labels=percentages, label_type='center', color=text_color, fontsize=10)

plt.tick_params(axis='y', labelsize=12)
ax.legend(ncol=4, bbox_to_anchor=(0, 1), frameon=False,
        fontsize='large', loc='lower left')
ax.text(x=76, y=-1.35, s="$\sqrt{s}$ = 13 TeV, 139 fb$^{-1}$ \nH -> WW*", ha='left', va='top', fontsize=12)

plt.tight_layout()
plt.savefig('bar-chart-fractions.pdf')
plt.close()

