% figures/feynman-graphs/HiggsProduction_GluonFusion.mp -- do not edit, generated automatically by t.tex
input feynmp
require_RCS_revision "1.30";
beginchar(1, 60*2.84526pt#, 22*2.84526pt#, 0);
"feynmf: 1";
LaTeX_unitlength:=2.84526pt;
subgraph (0, 0, w, h);
vinit;
pickup pencircle scaled thin;
vleft (__i1, __i2);
vright (__o1, __o2, __o3);
vconnect ("phantom", __i1, __v1, __o1);
vfreeze;
vconnect ("phantom", __i2, __v2, __o3);
vfreeze;
vconnect ("gluon, label=$g$, label.dist=+12.0", __i1, __v1);
vconnect ("gluon, label=$g$, label.dist=+12.0", __i2, __v2);
vconnect ("fermion, label=$t$, label.dist=-12.0", __v1, __v2, __v3, __v1);
vconnect ("dashes, label=$H$,plain", __v3, __o2);
vfreeze;
vdraw;
endsubgraph;
endchar;
% the end.
end.
endinput;
