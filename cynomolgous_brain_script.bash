#try automated skullstripping then cleaning up stripped brain with tkmedit
@NoisySkullStrip -input cyno+orig  -blur_fwhm 1
afni -niml -yesplugouts
suma -niml & 3dSkullStrip -input cyno+orig -o_ply anat_brain -visual -monkey -avoid_eyes -use_skull
3dcopy nu.nii cyno_stripped
tkmedit cyno+orig cyno_stripped+orig

#straight to tkmedit to perform manual skull stripping
tkmedit cyno nu.mgz  -aux T1.mgz

#convert back to .nii so we can look at things in afni
mri_convert nu.mgz nu.nii

#auto registration of stripped brain with d99 with -no_ss flag because we already did that and the atlas has no skull
@auto_tlrc -base D99_template.nii.gz -input nu.nii -no_ss

#visualize transformed cynomolgous brain with d99
freeview nu_at.nii nu.nii D99_template.nii.gz D99_segment.nii.gz D99_atlas_1.2b.nii.gz 
#load nu,atlas,template in afni to create gifs/pngs or to analyze ROI overlaps
afni


#guesses at next steps


#nu masked by D99_segment
3dcalc -a nu_at.nii -b D99_segment.nii.gz -expr 'a*bool(b)' -prefix nu_at_segment.nii
3dcalc -a nu_at_segment.nii -b D99_segment.nii.gz -expr 'b*bool(a)' -prefix nu_at_segment_labeled.nii

#nu_at_segment_labeled masked by D99_atlas
3dcalc -a nu_at_segment_labeled.nii -b D99_atlas_1.2b.nii.gz -expr 'b*bool(a)' -prefix nu_at_segment_atlas_labeled.nii


#nu_at_segment_atlas_labeled subtracted from nu_at_segment_labeled
3dcalc -a nu_at_segment_atlas_labeled.nii -b nu_at_segment_labeled.nii -expr 'b-a' -prefix nu_segment_atlas_negative.nii

#nu_segment_atlas_negative added to nu_at_segment_atlas_labeled
3dcalc -a nu_segment_atlas_negative.nii -b nu_at_segment_atlas_labeled.nii -expr 'a+b' -prefix nu_final.nii

freeview 


#register final brain back to original nu space
3dresample -input nu.nii -master cynomolgous_atlas.nii -prefix nu_upsampled.nii
#3dAllineate -base nu_upsample.nii -input nu_at_plus_template_segment_atlas.nii -prefix cynomolgous_atlas_at -final NN -cost crU
3dvolreg -base nu_upsampled.nii -input cynomolgous_atlas.nii -prefix cynomolgous_atlas_at -final NN
3dcopy cynomolgous_atlas_at.BRIK.gz cynomolgous_atlas_at.nii
freeview *.nii








3dcalc -a D99_atlas_1.2b.nii.gz -b D99_segment.nii.gz -expr 'b*bool(a)' -prefix D99_segment_masked_by_atlas.nii
3dcalc -a D99_segment_masked_by_atlas.nii -b D99_segment.nii.gz -expr 'b-a' -prefix D99_segment_minus_atlas.nii
3dcalc -a D99_atlas_1.2b.nii.gz -b D99_segment_minus_atlas.nii -expr 'a+b' -prefix D99_atlas_plus_segment.nii
3dresample -input nu.nii -master D99_atlas_plus_segment.nii -prefix nu_upsampled.nii
#3dvolreg -base nu_upsampled.nii -input D99_atlas_plus_segment.nii -prefix cynomolgous_atlas.nii -final NN
3dAllineate -1Dmatrix_apply nu_at.Xat_inverse.1D -prefix cynomolgous_atlas.nii -source D99_atlas_plus_segment.nii -master nu_upsampled.nii -final NN
freeview *.nii *.gz

