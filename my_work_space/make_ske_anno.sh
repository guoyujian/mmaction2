
#!/bin/sh
#============ get the file name ===========
src='/mmaction2/filling/val0110/'

dst_annos='/mmaction2/filling/val3_ske_annos/'
dst_videos='/mmaction2/filling/val3_ske_videos/'

for tmp in ${src}/*; do
    filename=`basename $tmp`

    pkl_filename=${filename/'.mp4'/'.pkl'}
    pkl_filename=${pkl_filename/'.MP4'/'.pkl'}
    pkl_filename=${pkl_filename/'.MOV'/'.pkl'}

    mp4_filename=${pkl_filename/'.pkl'/'.mp4'}
    cmd="python /mmaction2/demo/demo_skeleton.py ${src}${filename} ${dst_videos}${mp4_filename} ${dst_annos}${pkl_filename}"
    echo $cmd
    `$cmd`

    # `python /mmaction2/demo/demo_skeleton.py ${src}${filename} ${dst_videos}${filename} ${dst_annos}${dst_filename}`
    
    
done 