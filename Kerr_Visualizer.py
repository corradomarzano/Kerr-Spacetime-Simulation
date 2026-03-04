# Import nedded Libraries

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from numpy import pi,cos,sin

import plotly.graph_objects as go
from plotly.subplots import make_subplots

#############################################################################################################
# I/O strings for user communication

input_string = "\nInput your Kerr spacetime visualization choice:\n" \
"\n******************************************************************************\n" \
"1) For a single static plot using Matplotlib\n" \
"2) For an interactive plot with modifiable Black Hole's spin 'a' using Plotly.\n" \
"3) To use both representations.\n" \
"******************************************************************************\n" \
"\nYour input: "

error_string = "\n******************************************************************************\n" \
    f"Error! Your input is invalid. You must choose between '1', '2' or '3' as a visualization option." \
    "\n******************************************************************************"

#############################################################################################################
# Checking the validity of the user's input
while True:
    try:
        flag = int(input(input_string))
        
        if flag in (1, 2, 3):
            break
        else:
            print(error_string)
            
    except ValueError:
        print(error_string)
#############################################################################################################
# Case 1): Static representation
######################################################
# I/O strings for user communication in case 1.

input_string = "\nInput your Compact Object's mass (M>0) in Solar Mass units and the angular momentum per unit mass\nas a fraction of M (Schwarzschild = 0<=a<=1 = Extremal) as two numbers separated by a space: "

error_string = "\nError! Your input is invalid. You must input 'M' (M>0) and 'a' (Schwarzschild = 0<=a<=1 = Extremal) as two numbers separated by a space."
#####################################################
if flag in (1,3):
    fig = plt.figure(figsize=(11,12))
    ax = plt.axes(projection='3d')

    phi,theta = np.mgrid[0:2*pi:60j, 0:pi:30j]

    #Definiton of the Black Hole parameters ( in geometrized unit: c=G=1 )
    while True:
        try:
            M, a = map(float, input(input_string).split())
            
            if M>0 and 0<=a<=1.0:
                break
            else:
                print(error_string)
                
        except ValueError:
            print(error_string)

    #M = 1.0      #BH's mass in Solar Masses unit
    a = M*a    #a=J/M, 0<=a<=M

    # rsm <= rm <= rp <= rsp
    rp = M + np.sqrt(M**2 - a**2)
    rm = M - np.sqrt(M**2 - a**2)
    rsp = M + np.sqrt(M**2 - (a*cos(theta))**2)
    rsm = M - np.sqrt(M**2 - (a*cos(theta))**2)

    xp,yp,zp = rp*sin(theta)*sin(phi),rp*sin(theta)*cos(phi),rp*cos(theta)
    xm,ym,zm = rm*sin(theta)*sin(phi),rm*sin(theta)*cos(phi),rm*cos(theta)
    xsp,ysp,zsp = rsp*sin(theta)*sin(phi),rsp*sin(theta)*cos(phi),rsp*cos(theta)
    xsm,ysm,zsm = rsm*sin(theta)*sin(phi),rsm*sin(theta)*cos(phi),rsm*cos(theta)

    ax.plot_wireframe(xsp, ysp, zsp, color='green',alpha=0.15, label='Outer Ergosphere')
    ax.plot_wireframe(xp, yp, zp, color='blue',alpha=0.2, label='Outer Horizon')
    ax.plot_wireframe(xm, ym, zm, color='red',alpha=0.1, label='Inner Horizon')
    ax.plot_wireframe(xsm, ysm, zsm, color='orange', label='Inner Ergosphere')
    ax.plot(0,0,0,color='black',marker='o')

    ax.set_title('Kerr solution for a rotating Black Hole')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.legend(bbox_to_anchor=(1.2, 0.9))
    plt.show()

    print('\nM = {0} M_sun\na = {1} M_sun = {2}% M'.format(M,a,a/M*100))
    print('Outer Horizon: r+ = {0} M_sun'.format(np.round(rp,2)))
    print('Inner Horizon: r- = {0} M_sun\n'.format(np.round(rm,2)))

#############################################################################################################
# Case 2): Interactive plot
######################################################
# I/O strings for user communication in case 2.

input_string = "\nInput your Compact Object's mass (M>0) in Solar Mass units and the number of steps for the slider of the angular momentum\nper unit mass as a fraction of M (Schwarzschild = 0<=a<=1 = Extremal) (recommended n=11) as two numbers separated by a space: "

error_string = "\nError! Your input is invalid. You must input 'M' (M>0) and the number of steps for the 'a' slider n (positive integer) as two numbers separated by a space."
#####################################################
if flag in (2,3):
    #Definition of the angular coordinates
    phi = np.linspace(0, 2 * np.pi, 100)
    theta = np.linspace(0, np.pi, 50)
    theta, phi = np.meshgrid(theta, phi)

    #Definiton of the Black Hole parameters ( in geometrized unit: c=G=1 )
    while True:
        try:
            M, n = map(float, input(input_string).split())
            n = int(n)
            
            if M>0 and n>0:
                break
            else:
                print(error_string)
                
        except ValueError:
            print(error_string)
    
    #M = 1.0       #BH's mass in Solar Masses unit
    a = M*1.0     #a=J/M, 0<=a<=M, J=Black Hole's angular momentum

    # rsm <= rm <= rp <= rsp
    rp = M + np.sqrt(M**2 - a**2)                #Black Hole's Outer Horizon radius
    rm = M - np.sqrt(M**2 - a**2)                #Black Hole's Inner Horizon radius
    rsp = M + np.sqrt(M**2 - (a*cos(theta))**2)  #Black Hole's Outer Ergosphere radius
    rsm = M - np.sqrt(M**2 - (a*cos(theta))**2)  #Black Hole's Inner Ergosphere radius

    print('\nM = {0} M_sun\n# of steps = {1}\n'.format(M,n))

    #Coordinate change: Spherical -----> Cartesian
    xp,yp,zp = rp*sin(theta)*sin(phi),rp*sin(theta)*cos(phi),rp*cos(theta)        #Black Hole's Outer Horizon coordinates
    xm,ym,zm = rm*sin(theta)*sin(phi),rm*sin(theta)*cos(phi),rm*cos(theta)        #Black Hole's Inner Horizon coordinates
    xsp,ysp,zsp = rsp*sin(theta)*sin(phi),rsp*sin(theta)*cos(phi),rsp*cos(theta)  #Black Hole's Outer Ergosphere coordinates
    xsm,ysm,zsm = rsm*sin(theta)*sin(phi),rsm*sin(theta)*cos(phi),rsm*cos(theta)  #Black Hole's Inner Ergosphere coordinates

    # Create the 3D plot
    fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'surface'}]])

    # Outer Horizon
    surface1 = go.Surface(x=xp, y=yp, z=zp, opacity=0.3, showscale=False, name='Outer Horizon')
    fig.add_trace(surface1)

    # Inner Horizon
    surface2 = go.Surface(x=xm, y=ym, z=zm, opacity=0.35, showscale=False, name='Inner Horizon')
    fig.add_trace(surface2)

    # Outer Ergosphere
    surface3 = go.Surface(x=xsp, y=ysp, z=zsp, opacity=0.25, showscale=False, name='Outer Ergosphere')
    fig.add_trace(surface3)

    # Inner Ergosphere
    surface4 = go.Surface(x=xsm, y=ysm, z=zsm, opacity=0.8, showscale=False, name='Inner Ergosphere')
    fig.add_trace(surface4)

    # Add slider to dynamically change the value of the parameter a
    steps = []
    for i in np.linspace(0.0, 1.0, n):  # i is the factor that represents what percentage of M is a (i=0: Schwarzschild ; i=1: Extremal Black Hole)
        updated_rp = M + np.sqrt(M**2 - (a*i)**2)
        updated_rm = M - np.sqrt(M**2 - (a*i)**2)
        updated_rsp = M + np.sqrt(M**2 - (a*i*cos(theta))**2)
        updated_rsm = M - np.sqrt(M**2 - (a*i*cos(theta))**2)

        updated_xp,updated_yp,updated_zp = updated_rp*sin(theta)*sin(phi),updated_rp*sin(theta)*cos(phi),updated_rp*cos(theta)
        updated_xm,updated_ym,updated_zm = updated_rm*sin(theta)*sin(phi),updated_rm*sin(theta)*cos(phi),updated_rm*cos(theta)
        updated_xsp,updated_ysp,updated_zsp = updated_rsp*sin(theta)*sin(phi),updated_rsp*sin(theta)*cos(phi),updated_rsp*cos(theta)
        updated_xsm,updated_ysm,updated_zsm = updated_rsm*sin(theta)*sin(phi),updated_rsm*sin(theta)*cos(phi),updated_rsm*cos(theta)

        step = {'args': [{'x': [updated_xp,updated_xm,updated_xsp,updated_xsm], 'y': [updated_yp,updated_ym,updated_ysp,updated_ysm], 'z': [updated_zp,updated_zm,updated_zsp,updated_zsm]}],
                'label': f'a: {i:.2f} M',
                'method': 'restyle'}
        steps.append(step)

    sliders = [{
        'active': 0,
        'steps': steps,
        'pad': {'t': 50}
    }]

    # Update layout with sliders
    fig.update_layout(sliders=sliders)

    # Show the plot
    fig.show()