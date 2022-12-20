#!/bin/bash

 # Kill and Restart Server Proc by ID


function res_serve () {
	trap_sig=$(($? - 128))
	 echo "res_serve called ~ trap sig ~ ""$trap_sig"

	 serve_proc=""
        ps_line=$( ps -aux | grep silc_strp_bttp_serve  )
        ps_line_idx=0
       for entry in $ps_line
          do
                ps_line_idx=$((ps_line_idx+1))
                #echo "psline entry ${ps_line_idx}" ~ "$entry"
                if [ $ps_line_idx == 2 ];
                then echo "found strp_bttp_serve proc id for kill ~ ""$entry"
                        serve_proc=$entry
                        
			kill $entry
                        echo "restart serve"
	    		python3  /home/si/os_projects/3Trade_GIS/Silc_STR_Serve/silc_strp_bttp_serve.py &
		   echo "restarted pyttp serve success"
	   fi
   done
echo "res_serve complete"
}


exit_kill_serve (){
echo "kill serve exit call ~ "
exit
}

#Kill and do not restart for exit w sigint
function ps_kill_serve () {

	trap_sig=$(($?))
	echo "kill_serve called ~~  "$trap_sig


#	if [[ $( echo $trap_sig)  == 10 ]]:
#	then
#		echo " 10 ~ SIGUSR1"
#		#break for some reason
#		break
#	fi

	echo "grep silc serve ps -aux"
	serve_proc=""
        ps_line=$( ps -aux | grep silc_strp_bttp_serve  )
        ps_line_idx=0
         for entry in $ps_line
        do
                ps_line_idx=$((ps_line_idx+1))
                echo "psline entry ${ps_line_idx} ~ $entry"
                if [ $ps_line_idx == 2 ];
                then echo "found proc id for kill"
                        serve_proc=$entry
                        kill $entry
                        echo "serve killed"
                fi
done

exit
# Just call exit
#or grep for script ps works too
#	echo "grep for script proc"
#        ps_line=$( ps -aux | grep $0  )
#        
#	ps_line_idx=0
#       
#	for entry in $ps_line
#          do
#                ps_line_idx=$((ps_line_idx+1))
#                echo "psline script entry ${ps_line_idx}" ~ "$entry"
#                if [ $ps_line_idx == 2 ];
#                then echo "found script proc id for kill ~ ""$entry"
#                        serve_proc=$entry
#			kill $entry
#                        echo "kill script proc complete"
#	   fi
#	done


}

function log_err (){
	echo "call LOG TRAP ERR "
}

 while :
 	trap ps_kill_serve EXIT;	
	#ctl-c exit code 130, ctl-d never works
	#trap kill_serve SIGHUP SIGINT
	
	# ctl-c exic code 0, ctl-d not work
	#trap kill_serve 1 2 3 5 9  
 do
        old_cat_fs=""
        new_cat_fs=""

#	echo "shasum sh ~ ""$0"

 for diritem in $(find . -type f -print)
  do
    if [[ ${diritem} != *".swp" ]]; then
	#echo "get dir names rec ~ "$diritem
   	item_sum=" $(shasum $diritem)"
	#echo "get rec item shasum "$item_sum
   	old_cat_fs=$old_cat_fs$item_sum
    fi  
done
 #echo "Old Cat FS ~ "$old_cat_fs

sleep 3

 for diritem in $(find . -type f -print)
  do
	#echo "get new dir names rec ~ "$diritem
	if [[ ${diritem} != *".swp" ]]; then  
          item_sum=" $(shasum $diritem)"
	  #echo "get rec item shasum "$item_sum
          new_cat_fs=$new_cat_fs$item_sum
        fi
  done
  #echo "New Cat FS ~ "$new_cat_fs

 if [ "$old_cat_fs" == "$new_cat_fs" ];
   then
        echo '~ 0 ~' 
 else
         echo 'Fire Hot Reload Server '
          res_serve
 	echo "res serve continue"
 fi
 done

