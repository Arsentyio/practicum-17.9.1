{\rtf1\ansi\ansicpg1251\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;\f1\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red191\green100\blue38;\red32\green32\blue32;\red254\green187\blue91;
\red153\green168\blue186;\red117\green114\blue185;\red86\green132\blue173;\red88\green118\blue71;}
{\*\expandedcolortbl;;\csgenericrgb\c74902\c39216\c14902;\csgenericrgb\c12549\c12549\c12549;\csgenericrgb\c99608\c73333\c35686;
\csgenericrgb\c60000\c65882\c72941;\csgenericrgb\c45882\c44706\c72549;\csgenericrgb\c33725\c51765\c67843;\csgenericrgb\c34510\c46275\c27843;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs30 \cf2 \cb3 def \cf4 sorted_numbers\cf5 (inp):\
    \cf2 for \cf5 i \cf2 in \cf6 range\cf5 (\cf7 1\cf2 , \cf6 len\cf5 (inp)):\
        x = inp[i]\
        idx = i\
        \cf2 while \cf5 idx > \cf7 0 \cf2 and \cf5 inp[idx - \cf7 1\cf5 ] > x:\
            inp[idx] = inp[idx - \cf7 1\cf5 ]\
            idx = idx - \cf7 1\
        \cf5 inp[idx] = x\
    \cf2 return \cf5 inp\
\
\cf2 def \cf4 binary_search\cf5 (sequence\cf2 , \cf5 numb_from_seq\cf2 , \cf5 left\cf2 , \cf5 right):\
    \cf2 if \cf5 left > right:\
        \cf2 return \cf6 print\cf5 (\cf8 "
\f1 \uc0\u1063 \u1080 \u1089 \u1083 \u1086 
\f0  
\f1 \uc0\u1074 
\f0  
\f1 \uc0\u1089 \u1087 \u1080 \u1089 \u1082 \u1077 
\f0  
\f1 \uc0\u1085 \u1077 
\f0  
\f1 \uc0\u1085 \u1072 \u1081 \u1076 \u1077 \u1085 \u1086 
\f0 !"\cf5 )\
\
    middle = (right + left) // \cf7 2\
    \cf2 if \cf5 sequence[middle] == numb_from_seq:\
        \cf2 return \cf5 middle\
    \cf2 elif \cf5 numb_from_seq < sequence[middle]:\
        \cf2 return \cf5 binary_search(sequence\cf2 , \cf5 numb_from_seq\cf2 , \cf5 left\cf2 , \cf5 middle - \cf7 1\cf5 )\
    \cf2 else\cf5 :\
        \cf2 return \cf5 binary_search(sequence\cf2 , \cf5 numb_from_seq\cf2 , \cf5 middle + \cf7 1\cf2 , \cf5 right)\
\
numb = \cf6 input\cf5 (\cf8 '
\f1 \uc0\u1042 \u1074 \u1077 \u1076 \u1080 \u1090 \u1077 
\f0  
\f1 \uc0\u1095 \u1080 \u1089 \u1083 \u1072 
\f0  
\f1 \uc0\u1095 \u1077 \u1088 \u1077 \u1079 
\f0  
\f1 \uc0\u1087 \u1088 \u1086 \u1073 \u1077 \u1083 
\f0  '\cf5 ).split()\
sequence = \cf6 list\cf5 (\cf6 map\cf5 (\cf6 int\cf2 , \cf5 numb))\
sequence_sorted = sorted_numbers(sequence)\
\cf6 print\cf5 (\cf8 "
\f1 \uc0\u1057 \u1086 \u1079 \u1076 \u1072 \u1077 \u1084 
\f0  
\f1 \uc0\u1091 \u1087 \u1086 \u1088 \u1103 \u1076 \u1086 \u1095 \u1077 \u1085 \u1085 \u1099 \u1081 
\f0  
\f1 \uc0\u1089 \u1087 \u1080 \u1089 \u1086 \u1082 
\f0 :"\cf5 )\
\cf6 print\cf5 (sequence_sorted)\
numb_from_seq = \cf6 int\cf5 (\cf6 input\cf5 (\cf8 '
\f1 \uc0\u1042 \u1074 \u1077 \u1076 \u1080 \u1090 \u1077 
\f0  
\f1 \uc0\u1095 \u1080 \u1089 \u1083 \u1086 
\f0  
\f1 \uc0\u1076 \u1083 \u1103 
\f0  
\f1 \uc0\u1087 \u1086 \u1080 \u1089 \u1082 \u1072 
\f0  
\f1 \uc0\u1077 \u1075 \u1086 
\f0  
\f1 \uc0\u1074 
\f0  
\f1 \uc0\u1086 \u1089 \u1090 \u1086 \u1088 \u1090 \u1080 \u1088 \u1086 \u1074 \u1072 \u1085 \u1085 \u1086 \u1084 
\f0  
\f1 \uc0\u1089 \u1087 \u1080 \u1089 \u1082 \u1077 
\f0  '\cf5 ))\
id_numb = binary_search(sequence_sorted\cf2 , \cf5 numb_from_seq\cf2 , \cf7 0\cf2 , \cf6 len\cf5 (sequence_sorted))\
\cf6 print\cf5 (\cf8 "
\f1 \uc0\u1048 \u1085 \u1076 \u1077 \u1082 \u1089 
\f0  
\f1 \uc0\u1095 \u1080 \u1089 \u1083 \u1072 
\f0  
\f1 \uc0\u1074 
\f0  
\f1 \uc0\u1086 \u1090 \u1089 \u1086 \u1088 \u1090 \u1080 \u1088 \u1086 \u1074 \u1072 \u1085 \u1085 \u1086 \u1084 
\f0  
\f1 \uc0\u1089 \u1087 \u1080 \u1089 \u1082 \u1077 
\f0 : "\cf2 , \cf5 id_numb)\
\
}