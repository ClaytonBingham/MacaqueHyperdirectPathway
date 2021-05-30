import os
import numpy as np
from mayavi import mlab
from stl import mesh as npmesh
import math

def render_cynomolgous_brain(newfig=False,translate=[[0,0,0],[0,0]],scale=250,hemisphere='right',structures=['pial','stn','m1']):
	"""
	

	
	"""
	if hemisphere=='right':
		stn = np.array([-5.5,-5.2397,-4.35])*1000.0
	
	else:
		stn = np.array([6.05,-5.85,-4.35])*1000.0
	
	engine = mlab.get_engine()
	if newfig:
		fig = mlab.figure(engine=engine,bgcolor=(42/255.0,56/255.0,54/255.0),size=(1280*0.5,720*0.75))
	
	mlab.gcf().scene.parallel_projection = True
	
	if 'pial' in structures:
		rmesh_pial = npmesh.Mesh.from_file('.../BrainModel/cynomolgous_atlas_pial.stl')
		rmesh_pial.y-=173.5
		rmesh_pial.z-=122.5
		rmesh_pial.x-=137.5
		rmesh_pial.x*=scale
		rmesh_pial.y*=scale
		rmesh_pial.z*=scale
		rmesh_pial.rotate([0,0,1],math.radians(translate[1][0]))
		rmesh_pial.rotate([1,0,0],math.radians(translate[1][1]))
		rmesh_pial.x+=translate[0][0]-stn[0]
		rmesh_pial.y+=translate[0][1]-stn[1]
		rmesh_pial.z+=translate[0][2]-stn[2]-4000
		rmesh_pial.save('newmacaquemesh_pial.stl')
		dat_pial = engine.open('newmacaquemesh_pial.stl')
		surf_pial = mlab.pipeline.surface(dat_pial,opacity=0.0,color=(114/255.0, 159/255.0, 207/255.0),representation='surface',line_width=0.5)
		cut_pial = mlab.pipeline.scalar_cut_plane(surf_pial,plane_orientation='z_axes')
		cut_pial.implicit_plane.widget.enabled=False
		
	if 'stn' in structures:
		rmesh_stn_right = npmesh.Mesh.from_file('.../BrainModel/cynomolgous_atlas_stn_right.stl')
		rmesh_stn_right.y-=173.5
		rmesh_stn_right.z-=122.5
		rmesh_stn_right.x-=137.5
		rmesh_stn_right.x*=scale
		rmesh_stn_right.y*=scale
		rmesh_stn_right.z*=scale
		rmesh_stn_right.rotate([0,0,1],math.radians(translate[1][0]))
		rmesh_stn_right.rotate([1,0,0],math.radians(translate[1][1]))
		rmesh_stn_right.x+=translate[0][0]-stn[0]
		rmesh_stn_right.y+=translate[0][1]-stn[1]
		rmesh_stn_right.z+=translate[0][2]-stn[2]-4000
		rmesh_stn_right.save('newmacaquemesh_stn_right.stl')
		
		rmesh_stn_left = npmesh.Mesh.from_file('.../BrainModel/cynomolgous_atlas_stn_left.stl')
		rmesh_stn_left.y-=173.5
		rmesh_stn_left.z-=122.5
		rmesh_stn_left.x-=137.5
		rmesh_stn_left.x*=scale
		rmesh_stn_left.y*=scale
		rmesh_stn_left.z*=scale
		rmesh_stn_left.rotate([0,0,1],math.radians(translate[1][0]))
		rmesh_stn_left.rotate([1,0,0],math.radians(translate[1][1]))
		rmesh_stn_left.x+=translate[0][0]-stn[0]
		rmesh_stn_left.y+=translate[0][1]-stn[1]
		rmesh_stn_left.z+=translate[0][2]-stn[2]-4000
		rmesh_stn_left.save('newmacaquemesh_stn_left.stl')
			
		dat_stn_right = engine.open('newmacaquemesh_stn_right.stl')
		surf_stn_right = mlab.pipeline.surface(dat_stn_right,opacity=0.05,color=(179/255.0, 33/255.0, 7/255.0),representation='wireframe',line_width=0.5)
		surf_stn_right.actor.property.frontface_culling = True
		surf_stn_right.actor.property.backface_culling = True

		dat_stn_left = engine.open('newmacaquemesh_stn_left.stl')
		surf_stn_left = mlab.pipeline.surface(dat_stn_left,opacity=0.05,color=(179/255.0, 33/255.0, 7/255.0),representation='wireframe',line_width=0.5)
		surf_stn_left.actor.property.frontface_culling = True
		surf_stn_left.actor.property.backface_culling = True
	
	if 'm1' in structures:
		rmesh_m1_right = npmesh.Mesh.from_file('.../BrainModel/cynomolgous_atlas_m1_right.stl')
		rmesh_m1_right.y-=173.5
		rmesh_m1_right.z-=122.5
		rmesh_m1_right.x-=137.5
		rmesh_m1_right.x*=scale
		rmesh_m1_right.y*=scale
		rmesh_m1_right.z*=scale
		rmesh_m1_right.rotate([0,0,1],math.radians(translate[1][0]))
		rmesh_m1_right.rotate([1,0,0],math.radians(translate[1][1]))
		rmesh_m1_right.x+=translate[0][0]-stn[0]
		rmesh_m1_right.y+=translate[0][1]-stn[1]
		rmesh_m1_right.z+=translate[0][2]-stn[2]-4000
		rmesh_m1_right.save('newmacaquemesh_m1_right.stl')

		rmesh_m1_left = npmesh.Mesh.from_file('.../BrainModel/cynomolgous_atlas_m1_left.stl')
		rmesh_m1_left.y-=173.5
		rmesh_m1_left.z-=122.5
		rmesh_m1_left.x-=137.5
		rmesh_m1_left.x*=scale
		rmesh_m1_left.y*=scale
		rmesh_m1_left.z*=scale
		rmesh_m1_left.rotate([0,0,1],math.radians(translate[1][0]))
		rmesh_m1_left.rotate([1,0,0],math.radians(translate[1][1]))
		rmesh_m1_left.x+=translate[0][0]-stn[0]
		rmesh_m1_left.y+=translate[0][1]-stn[1]
		rmesh_m1_left.z+=translate[0][2]-stn[2]-4000
		rmesh_m1_left.save('newmacaquemesh_m1_left.stl')
		
#		dat_m1_right = engine.open('newmacaquemesh_m1_right.stl')
#		surf_m1_right = mlab.pipeline.surface(dat_m1_right,opacity=1.0,color=(82/255.0, 191/255.0, 95/255.0),representation='surface',line_width=0.5)
#		cut_m1_right = mlab.pipeline.scalar_cut_plane(surf_m1_right,plane_orientation='z_axes')
#		cut_m1_right.implicit_plane.widget.enabled=True
#		
#		dat_m1_left = engine.open('newmacaquemesh_m1_left.stl')
#		surf_m1_left = mlab.pipeline.surface(dat_m1_left,opacity=1.0,color=(82/255.0, 160/255.0, 191/255.0),representation='surface',line_width=0.5)
#		cut_m1_left = mlab.pipeline.scalar_cut_plane(surf_m1_left,plane_orientation='z_axes')
#		cut_m1_left.implicit_plane.widget.enabled=True



def get_shift_rotate_dict_for_swcs():
	sr_dict = {}
	#right
	sr_dict['/home/clayton/Desktop/Coude_full/post_neotube_11_11_19/1-2.swc'] = [[3050,-2275,-500],[0,-180,0]]
	sr_dict['/home/clayton/Desktop/Coude_full/post_neotube_11_11_19/3_D-13.swc'] = [[-11500,2550,200],[-5,-180,0]]
	sr_dict['/home/clayton/Desktop/Coude_full/post_neotube_11_11_19/3_D-15.swc'] = [[-12050,4050,200],[15,-180,0]]
	sr_dict['/home/clayton/Desktop/Coude_full/post_neotube_11_11_19/4-22.swc'] = [[-3400,-700,-18000],[-8,-170,0]]
	sr_dict['/home/clayton/Desktop/Coude_full/post_neotube_11_11_19/4-19.swc'] = [[-2150,-700,-18250],[0,-170,0]]
	sr_dict['/home/clayton/Desktop/Coude_full/post_neotube_11_11_19/1-1.swc'] = [[3700,-1250,-400],[0,-180,0]]
	sr_dict['/home/clayton/Desktop/Coude_full/post_neotube_11_11_19/4-21.swc'] = [[-3000,500,-18500],[-10,-150,0]]
	sr_dict['/home/clayton/Desktop/Coude_full/post_neotube_11_11_19/3_D-14.swc'] = [[-13500,4050,200],[0,-180,0]]
	sr_dict['/home/clayton/Desktop/Coude_full/post_neotube_11_11_19/1-3.swc'] = [[4550,-1800,0],[10,-180,0]]
	sr_dict['/home/clayton/Desktop/Coude_full/post_neotube_11_11_19/4-23.swc'] = [[-1700,550,-18000],[10,-170,0]]
	sr_dict['/home/clayton/Desktop/Coude_full/post_neotube_11_11_19/2-11.swc'] = [[7050,-4800,0],[-30,-160,0]]
	sr_dict['/home/clayton/Desktop/Coude_full/post_neotube_11_11_19/2-12.swc'] = [[7750,-4800,900],[-30,-160,35]]
	sr_dict['/home/clayton/Desktop/Coude_full/post_neotube_11_11_19/4-24.swc'] = [[3000,1750,-18000],[-15,-170,0]]
	sr_dict['/home/clayton/Desktop/Coude_full/post_neotube_11_11_19/4-20.swc'] = [[-1500,600,-18000],[5,-170,0]]
	
	#left
	sr_dict['/home/clayton/Desktop/Coude_full/post_neotube_11_11_19/1_D-7.swc'] = [[-21500,-27500,0],[0,0,-17]]
	sr_dict['/home/clayton/Desktop/Coude_full/post_neotube_11_11_19/1_D-10.swc'] = [[-22250,-27500,-500],[0,0,-12]]
	sr_dict['/home/clayton/Desktop/Coude_full/post_neotube_11_11_19/3-17.swc'] = [[0,-50,0],[0,0,-12]]
	sr_dict['/home/clayton/Desktop/Coude_full/post_neotube_11_11_19/1_D-8.swc'] = [[-21500,-27500,-500],[0,0,-12]]
	sr_dict['/home/clayton/Desktop/Coude_full/post_neotube_11_11_19/3-16.swc'] = [[0,-50,0],[6,0,-12]]
	sr_dict['/home/clayton/Desktop/Coude_full/post_neotube_11_11_19/1_D-5.swc'] = [[-22000,-27500,-500],[0,0,-6]]
	sr_dict['/home/clayton/Desktop/Coude_full/post_neotube_11_11_19/1_D-9.swc'] = [[-21250,-27500,-500],[0,0,-20]]
	sr_dict['/home/clayton/Desktop/Coude_full/post_neotube_11_11_19/3-18.swc'] = [[0,-50,0],[5,2,-12]]
	sr_dict['/home/clayton/Desktop/Coude_full/post_neotube_11_11_19/1_D-6.swc'] = [[-22250,-27500,-500],[-5,15,-12]]
	sr_dict['/home/clayton/Desktop/Coude_full/post_neotube_11_11_19/1_D-4.swc'] = [[-21500,-27500,-500],[0,0,-16]]
	return(sr_dict)



