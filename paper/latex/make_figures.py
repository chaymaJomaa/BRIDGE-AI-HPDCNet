from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm, Normalize
import numpy as np

out=Path('/mnt/data/hpdc_ieee_article/figures')
labels=['BS','EB','LB','LM','SL','SM','TS','YLCV','TMV','H']
b=np.array([
[211,0,0,0,2,0,1,0,0,0],
[0,100,0,0,0,0,0,0,0,0],
[0,0,192,0,0,0,0,0,0,0],
[0,0,1,95,0,0,0,0,0,0],
[0,0,0,0,177,1,0,0,0,0],
[0,0,0,0,0,165,2,0,1,0],
[0,0,0,0,0,2,140,0,0,0],
[0,0,0,0,0,0,0,537,0,0],
[0,0,0,0,0,0,0,0,38,0],
[0,0,0,0,0,0,0,0,0,160]
], dtype=int)
p=np.array([
[212,0,1,0,0,0,1,0,0,0],
[0,99,1,0,0,0,0,0,0,0],
[0,0,192,0,0,0,0,0,0,0],
[0,0,0,96,0,0,0,0,0,0],
[0,0,1,0,177,0,0,0,0,0],
[0,0,0,0,0,164,4,0,0,0],
[0,0,0,0,0,0,141,0,0,1],
[0,0,0,0,0,0,0,537,0,0],
[0,0,0,0,0,0,0,0,38,0],
[0,0,0,0,0,0,0,0,0,160]
], dtype=int)
assert b.sum() == 1825 and p.sum()==1825
assert b.trace()==1815 and p.trace()==1816
print('Confusion matrix checks:', b.sum(), b.trace(), p.trace())

plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':8, 'pdf.fonttype':42,'ps.fonttype':42})
for matrix,name,file in [(b,'Reproduced baseline','confusion_baseline.pdf'),(p,'Proposed lightweight variant','confusion_proposed.pdf')]:
    fig,ax=plt.subplots(figsize=(4.3,3.8))
    im=ax.imshow(matrix,cmap='Blues',vmin=0,vmax=540,interpolation='nearest')
    ax.set_xticks(np.arange(10));ax.set_xticklabels(labels, rotation=55,ha='right',fontsize=7)
    ax.set_yticks(np.arange(10));ax.set_yticklabels(labels,fontsize=7)
    ax.set_xlabel('Predicted class',fontsize=8);ax.set_ylabel('True class',fontsize=8)
    for i in range(10):
        for j in range(10):
            if matrix[i,j]:
                ax.text(j,i,str(matrix[i,j]),ha='center',va='center',fontsize=7,
                        color=('white' if matrix[i,j]>=200 else '#16202b'))
    ax.set_xticks(np.arange(-.5,10,1), minor=True)
    ax.set_yticks(np.arange(-.5,10,1), minor=True)
    ax.grid(which='minor',color='white',linewidth=.6)
    ax.tick_params(which='both',length=0)
    fig.tight_layout(pad=0.7)
    fig.savefig(out/file,bbox_inches='tight')
    fig.savefig(out/file.replace('.pdf','.png'),dpi=220,bbox_inches='tight')
    plt.close(fig)

fig,ax=plt.subplots(figsize=(4,2.3))
model=['Parameters','MACs','GPU latency']
base=np.array([100.,100.,100.])
prop=np.array([115544/764376*100, .2028/1.0147*100, 5.7231/8.3623*100])
x=np.arange(3)
width=.32
rects1=ax.bar(x-width/2,base,width,label='Baseline',color='#9baec0')
rects2=ax.bar(x+width/2,prop,width,label='Proposed',color='#2368a0')
for rect in list(rects1)+list(rects2):
    val=rect.get_height()
    ax.annotate(f'{val:.1f}%',(rect.get_x()+rect.get_width()/2,val),textcoords='offset points',xytext=(0,3),ha='center',fontsize=7)
ax.set_xticks(x);ax.set_xticklabels(model,fontsize=8)
ax.set_ylim(0,119)
ax.set_ylabel('Relative to baseline (%)',fontsize=8)
ax.grid(axis='y',alpha=.25)
ax.set_axisbelow(True)
ax.legend(loc='upper right',ncol=2,fontsize=7,frameon=False)
fig.tight_layout(pad=1)
fig.savefig(out/'efficiency.pdf',bbox_inches='tight')
fig.savefig(out/'efficiency.png',dpi=220,bbox_inches='tight')
plt.close(fig)
