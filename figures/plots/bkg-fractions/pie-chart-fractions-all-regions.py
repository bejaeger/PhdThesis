import numpy as np
import matplotlib.pyplot as plt

labels = {
    "s_Vgamma_step": "$V\gamma$",
    "s_Misid_step": "Mis-Id",
    "s_otherVV_step": "Other $VV$",
    "s_Zjets_step": "$Z/\gamma*$",
    "s_WW_step": "$WW$ (Strong)",
    "s_EWWW_step": "$WW$ (EW)",
    "s_singletop_step": "$Wt$",
    "s_ttbar_step": "$t\\bar{t}$",
    "s_vbf_step": "$H_{\mathrm{VBF}}$",
    "s_ggF_step": "$H_{\mathrm{ggF}}$"}
# "Mis-Id"

colors = {
    "s_Misid_step": "#3DFDFF",# sns.color_palette("Paired")[9], # vgamma purple    
    "s_Vgamma_step": "#6A3D9A",# sns.color_palette("Paired")[9], # vgamma purple
    #"s_otherVV_step": "#CAB2D6",# sns.color_palette("Paired")[8], # other VV light purple
    "s_otherVV_step": "#6A3D9A",# sns.color_palette("Paired")[8], # other VV light purple
    "s_Zjets_step": "#33A02C",  # sns.color_palette("Paired")[3], # Zjets green
    "s_WW_step": "#2578B4",  # sns.color_palette("Paired")[1],  # WW blue
    "s_EWWW_step": "#A5CEE3",# sns.color_palette("Paired")[0], # EW WW light blue
    "s_singletop_step": "#FCFF99",# sns.color_palette("Paired")[10], # singletop light yellow
    "s_ttbar_step": "#FBD930",  # sns.color_palette("Set2")[5], # ttbar yellow
    "s_vbf_step": "#FA7F00",  # sns.color_palette("Paired")[7]] # VBF orange
    "s_ggF_step": "#E31E1C"  # sns.color_palette("Paired")[5], # ggF red
}

# EW WW in VBF region is 2.3467216

new = {
    "s_vbf_step": 31.93741936348283,
    "s_ggF_step": 2.777131487173932,
    "s_ttbar_step": 2.558835041783823,
    "s_singletop_step": 0.26581375279829444,
    "s_EWWW_step": 2.475628735952853,
    "s_WW_step": 1.7799693956367264,
    "s_Zjets_step": 2.1628455964441855,
    #"s_Vgamma_step": 0.5875710478841825,
    "s_otherVV_step": 0.5413627730276858 + 0.5875710478841825, 
    "s_Misid_step":1.2
    }  # , "Total": 45.0865771941845}

# old = {"s_vbf_step": 28.494697851203085,"s_ggF_step": 2.4607162123537876,"s_ttbar_step": 1.971413766794285,"s_singletop_step": 1.1005227737132373,"s_EWWW_step": 3.1742690567317595,"s_WW_step": 1.9417058186504619,"s_Zjets_step": 0.9098366812399945,"s_Vgamma_step": 0.0,"s_otherVV_step": 0.27922301128438676} #, "Total": 40.332385171971}
old = {"s_vbf_step": 28.494697851203085,
       "s_ggF_step": 2.4607162123537876,
       "s_ttbar_step": 1.971413766794285,
       "s_singletop_step": 1.1005227737132373,
       "s_EWWW_step": 3.3742690567317595,
       "s_WW_step": 1.9417058186504619,
       "s_Zjets_step": 0.9098366812399945,
       #"s_Vgamma_step": 0.0,
       "s_otherVV_step": 0.27922301128438676, 
       "s_Misid_step": 1.2
       }  # , "Total": 40.332385171971}


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
print(chosen.keys())
colors = [colors[n] for n in chosen.keys()]
labels = [labels[n] for n in chosen.keys()]
sizes = chosen.values()
# only "explode" the 2nd slice (i.e. 'Hogs')

# ggF is 3
explode = (0.05, 0, 0, 0, 0.2, 0, 0, 0, 0)
#explode = (0.2, 0.05, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2)

def func(pct, allvals):
    absolute = np.round(pct/100.*np.sum(allvals), 1)
    return "{:.1f}%\n({:.1f})".format(pct, absolute)

fig1, ax1 = plt.subplots()
patches, texts, autotexts = ax1.pie(sizes, explode=explode, labels=labels, #autopct='%1.1f%%',
        autopct=lambda pct: func(pct, sizes),
        shadow=False, startangle=90, colors=colors, labeldistance=1.1, pctdistance=0.73)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


plt.setp(texts, size=14)
plt.setp(autotexts, size=10, weight="bold")
plt.setp(patches, linewidth=0.1)

autotexts[2].set_fontsize(8) # MisId
autotexts[3].set_color('white') # WW

if not plotNew: 
    texts[6].set_text(texts[6].get_text()+" ("+autotexts[6].get_text().replace("\n", "")+")")
    autotexts[6].set_text('') # Zjets

autotexts[6].set_color('white') # Zjets
autotexts[1].set_color('white') # ggF

texts[6].set_position((texts[6].get_position()[0]-0.07, texts[6].get_position()[1]+0.05)) # Zjets
autotexts[5].set_text('') # Wt
texts[5].set_position((texts[5].get_position()[0]-0.07, texts[5].get_position()[1]+0.01)) # Wt


#autotexts[0].set_text('') # Vgamma
autotexts[8].set_text('') # other VV
texts[8].set_position((texts[8].get_position()[0]-0.14, texts[8].get_position()[1]+0.06)) # other VV
texts[7].set_position((texts[7].get_position()[0]-0.01, texts[7].get_position()[1]-0.02)) # ttbar

# plt.show()
if plotNew:
    plt.savefig('pie-chart-fractions-new.pdf')
else:
    plt.savefig('pie-chart-fractions-old.pdf')

