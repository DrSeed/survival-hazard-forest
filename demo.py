import os,numpy as np,matplotlib;matplotlib.use("Agg")
import matplotlib.pyplot as plt
os.makedirs("figures",exist_ok=True);os.makedirs("results",exist_ok=True)
rng=np.random.default_rng(6)
vars_=["Age >65","Stage III/IV","High CXCL9","Male","Smoker","Mutation X"]
hr=np.array([1.4,2.6,1.8,1.1,1.5,0.7])
lo=hr*rng.uniform(0.6,0.85,len(hr));hi=hr*rng.uniform(1.15,1.5,len(hr))
y=np.arange(len(vars_))
plt.figure(figsize=(7,4))
for i in range(len(vars_)):
    plt.plot([lo[i],hi[i]],[y[i],y[i]],c="k")
    plt.scatter(hr[i],y[i],s=60,c="firebrick",zorder=3)
plt.axvline(1,ls="--",c="grey");plt.yticks(y,vars_);plt.xscale("log")
plt.xlabel("hazard ratio (log)");plt.title("Cox hazard ratios (demo data)")
plt.tight_layout();plt.savefig("figures/demo.png",dpi=150)
open("results/summary.txt","w").write("6 covariates, hazard ratios\n");print("ok")