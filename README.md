# Bio-SystemII-Tokyo-Tech
This is the bio-system II lecture provided by Tokyo Tech 2021. This repo is using feet data for muscle analysis.  

### Model Discriptions:

we only consider the left leg model for analysis.
Joint structure model is considerd,
If there are multiple markers for the same joint, choose one for simpification.
#### Use L.ankle and L.knee

#### Center of Gravity:
Because there is no toe data, usetreat thenar as toe

* Thenar-heel=foot CG

* L.ankle-L.knee=leg CG

* L.ankle=joint ankle

* L.knee=joint knee

Ignore the angle between the moving path and x axis, so we can delete the y axis to make the model to 2D
#### Only consider time 1.16-1.496s
The coordinate system of the marker and the force file is the same
