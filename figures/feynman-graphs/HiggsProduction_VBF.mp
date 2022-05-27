% figures/feynman-graphs/HiggsProduction_VBF.mp -- do not edit, generated automatically by t.tex
input feynmp
require_RCS_revision "1.30";
beginchar(1, 60*2.84526pt#, 25*2.84526pt#, 0);
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
straight_galleries;
vconnect ("phantom", __v1, __v3, __v2);
vfreeze;
vconnect ("fermion, label=$q$", __i1, __v1);
vconnect ("fermion, label=$q$", __i2, __v2);
vconnect ("fermion, label=$q^\prime $", __v1, __o1);
vconnect ("fermion, label=$q^\prime $", __v2, __o3);
vconnect ("boson, label=$W/Z$", __v1, __v3, __v2);
vfreeze;
vconnect ("dashes, label=$H$,plain", __v3, __o2);
vfreeze;
vdraw;
endsubgraph;
endchar;
% the end.
end.
endinput;
