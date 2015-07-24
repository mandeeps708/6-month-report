## -*- encoding: utf-8 -*-
# This file was *autogenerated* from the file matrix.sagetex.sage
from sage.all_cmdline import *   # import sage library
_sage_const_180 = Integer(180); _sage_const_181 = Integer(181); _sage_const_182 = Integer(182); _sage_const_618 = Integer(618); _sage_const_344 = Integer(344); _sage_const_855 = Integer(855); _sage_const_824 = Integer(824); _sage_const_110 = Integer(110); _sage_const_117 = Integer(117); _sage_const_598 = Integer(598); _sage_const_539 = Integer(539); _sage_const_620 = Integer(620); _sage_const_623 = Integer(623); _sage_const_624 = Integer(624); _sage_const_532 = Integer(532); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_16 = Integer(16); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_19 = Integer(19); _sage_const_18 = Integer(18); _sage_const_817 = Integer(817); _sage_const_100 = Integer(100); _sage_const_102 = Integer(102); _sage_const_229 = Integer(229); _sage_const_526 = Integer(526); _sage_const_523 = Integer(523); _sage_const_836 = Integer(836); _sage_const_830 = Integer(830); _sage_const_66 = Integer(66); _sage_const_67 = Integer(67); _sage_const_64 = Integer(64); _sage_const_65 = Integer(65); _sage_const_62 = Integer(62); _sage_const_63 = Integer(63); _sage_const_60 = Integer(60); _sage_const_61 = Integer(61); _sage_const_68 = Integer(68); _sage_const_69 = Integer(69); _sage_const_230 = Integer(230); _sage_const_234 = Integer(234); _sage_const_726 = Integer(726); _sage_const_722 = Integer(722); _sage_const_802 = Integer(802); _sage_const_75 = Integer(75); _sage_const_74 = Integer(74); _sage_const_71 = Integer(71); _sage_const_70 = Integer(70); _sage_const_73 = Integer(73); _sage_const_72 = Integer(72); _sage_const_546 = Integer(546); _sage_const_548 = Integer(548); _sage_const_798 = Integer(798); _sage_const_811 = Integer(811); _sage_const_732 = Integer(732); _sage_const_40 = Integer(40); _sage_const_41 = Integer(41); _sage_const_42 = Integer(42); _sage_const_43 = Integer(43); _sage_const_44 = Integer(44); _sage_const_45 = Integer(45); _sage_const_46 = Integer(46); _sage_const_47 = Integer(47); _sage_const_48 = Integer(48); _sage_const_49 = Integer(49); _sage_const_155 = Integer(155); _sage_const_318 = Integer(318); _sage_const_310 = Integer(310); _sage_const_159 = Integer(159); _sage_const_277 = Integer(277); _sage_const_372 = Integer(372); _sage_const_278 = Integer(278); _sage_const_863 = Integer(863); _sage_const_783 = Integer(783); _sage_const_59 = Integer(59); _sage_const_58 = Integer(58); _sage_const_57 = Integer(57); _sage_const_56 = Integer(56); _sage_const_55 = Integer(55); _sage_const_54 = Integer(54); _sage_const_53 = Integer(53); _sage_const_52 = Integer(52); _sage_const_51 = Integer(51); _sage_const_50 = Integer(50); _sage_const_124 = Integer(124); _sage_const_306 = Integer(306); _sage_const_304 = Integer(304); _sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_28 = Integer(28); _sage_const_29 = Integer(29); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_26 = Integer(26); _sage_const_27 = Integer(27); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_702 = Integer(702); _sage_const_572 = Integer(572); _sage_const_849 = Integer(849); _sage_const_602 = Integer(602); _sage_const_842 = Integer(842); _sage_const_39 = Integer(39); _sage_const_38 = Integer(38); _sage_const_31 = Integer(31); _sage_const_30 = Integer(30); _sage_const_33 = Integer(33); _sage_const_32 = Integer(32); _sage_const_35 = Integer(35); _sage_const_34 = Integer(34); _sage_const_37 = Integer(37); _sage_const_36 = Integer(36); _sage_const_779 = Integer(779); _sage_const_677 = Integer(677); _sage_const_674 = Integer(674)## This file (matrix.sagetex.sage) was *autogenerated* from matrix.tex with sagetex.sty version 2012/01/16 v2.3.3-69dcb0eb93de.
import sagetex
_st_ = sagetex.SageTeXProcessor('matrix', version='2012/01/16 v2.3.3-69dcb0eb93de', version_check=True)
_st_.blockbegin()
try:
 m=var('m')
 n=var('n')
except:
 _st_.goboom(_sage_const_47 )
_st_.blockend()
try:
 _st_.inline(_sage_const_0 , latex(m))
except:
 _st_.goboom(_sage_const_52 )
try:
 _st_.inline(_sage_const_1 , latex(n))
except:
 _st_.goboom(_sage_const_52 )
try:
 _st_.inline(_sage_const_2 , latex(m))
except:
 _st_.goboom(_sage_const_53 )
try:
 _st_.inline(_sage_const_3 , latex(n))
except:
 _st_.goboom(_sage_const_53 )
try:
 _st_.inline(_sage_const_4 , latex(m))
except:
 _st_.goboom(_sage_const_55 )
try:
 _st_.inline(_sage_const_5 , latex(m))
except:
 _st_.goboom(_sage_const_55 )
try:
 _st_.inline(_sage_const_6 , latex(m!=n))
except:
 _st_.goboom(_sage_const_70 )
try:
 _st_.inline(_sage_const_7 , latex(m==_sage_const_1 ))
except:
 _st_.goboom(_sage_const_71 )
try:
 _st_.inline(_sage_const_8 , latex(n>_sage_const_1 ))
except:
 _st_.goboom(_sage_const_72 )
try:
 _st_.inline(_sage_const_9 , latex(m>_sage_const_1 ))
except:
 _st_.goboom(_sage_const_73 )
try:
 _st_.inline(_sage_const_10 , latex(n==_sage_const_1 ))
except:
 _st_.goboom(_sage_const_74 )
try:
 _st_.inline(_sage_const_11 , latex(m==n))
except:
 _st_.goboom(_sage_const_75 )
_st_.blockbegin()
try:
 a=matrix([[_sage_const_1 ,_sage_const_2 ,_sage_const_3 ],[_sage_const_1 ,_sage_const_2 ,_sage_const_4 ],[_sage_const_6 ,_sage_const_2 ,_sage_const_3 ]])
 b=matrix([[_sage_const_3 ,_sage_const_4 ],[_sage_const_1 ,_sage_const_2 ]])
 c=matrix([[_sage_const_3 ],[_sage_const_4 ],[_sage_const_1 ]])
 d=matrix([[_sage_const_3 ,_sage_const_4 ,_sage_const_1 ,_sage_const_2 ]])
 e=matrix([[_sage_const_7 ,_sage_const_4 ,_sage_const_4 ],[_sage_const_2 ,_sage_const_4 ,_sage_const_5 ],[_sage_const_3 ,_sage_const_5 ,_sage_const_6 ]])
except:
 _st_.goboom(_sage_const_100 )
_st_.blockend()
try:
 _st_.inline(_sage_const_12 , latex(a))
except:
 _st_.goboom(_sage_const_102 )
try:
 _st_.inline(_sage_const_13 , latex(b))
except:
 _st_.goboom(_sage_const_110 )
try:
 _st_.inline(_sage_const_14 , latex(c))
except:
 _st_.goboom(_sage_const_117 )
try:
 _st_.inline(_sage_const_15 , latex(d))
except:
 _st_.goboom(_sage_const_124 )
try:
 _st_.inline(_sage_const_16 , latex(a))
except:
 _st_.goboom(_sage_const_155 )
try:
 _st_.inline(_sage_const_17 , latex(_sage_const_4 *a))
except:
 _st_.goboom(_sage_const_159 )
try:
 _st_.inline(_sage_const_18 , latex(a))
except:
 _st_.goboom(_sage_const_180 )
try:
 _st_.inline(_sage_const_19 , latex(e))
except:
 _st_.goboom(_sage_const_181 )
try:
 _st_.inline(_sage_const_20 , latex(a))
except:
 _st_.goboom(_sage_const_182 )
try:
 _st_.inline(_sage_const_21 , latex(e))
except:
 _st_.goboom(_sage_const_182 )
try:
 _st_.inline(_sage_const_22 , latex(a+e))
except:
 _st_.goboom(_sage_const_182 )
try:
 _st_.inline(_sage_const_23 , latex(a))
except:
 _st_.goboom(_sage_const_229 )
try:
 _st_.inline(_sage_const_24 , latex(e))
except:
 _st_.goboom(_sage_const_230 )
try:
 _st_.inline(_sage_const_25 , latex(a*e))
except:
 _st_.goboom(_sage_const_234 )
try:
 _st_.inline(_sage_const_26 , latex(a))
except:
 _st_.goboom(_sage_const_277 )
try:
 _st_.inline(_sage_const_27 , latex(a.transpose()))
except:
 _st_.goboom(_sage_const_278 )
try:
 _st_.inline(_sage_const_28 , latex(a))
except:
 _st_.goboom(_sage_const_304 )
try:
 _st_.inline(_sage_const_29 , latex(c))
except:
 _st_.goboom(_sage_const_304 )
try:
 _st_.inline(_sage_const_30 , latex(a))
except:
 _st_.goboom(_sage_const_306 )
try:
 _st_.inline(_sage_const_31 , latex(c))
except:
 _st_.goboom(_sage_const_306 )
try:
 _st_.inline(_sage_const_32 , latex(a*c))
except:
 _st_.goboom(_sage_const_306 )
try:
 _st_.inline(_sage_const_33 , latex((a*c).transpose()))
except:
 _st_.goboom(_sage_const_310 )
try:
 _st_.inline(_sage_const_34 , latex(a))
except:
 _st_.goboom(_sage_const_318 )
try:
 _st_.inline(_sage_const_35 , latex(c))
except:
 _st_.goboom(_sage_const_318 )
try:
 _st_.inline(_sage_const_36 , latex((a*c).transpose()))
except:
 _st_.goboom(_sage_const_318 )
try:
 _st_.inline(_sage_const_37 , latex(matrix([[_sage_const_3 ,_sage_const_1 ,_sage_const_2 ],[_sage_const_1 ,_sage_const_4 ,_sage_const_0 ],[_sage_const_2 ,_sage_const_0 ,_sage_const_3 ]])))
except:
 _st_.goboom(_sage_const_344 )
try:
 _st_.inline(_sage_const_38 , latex(matrix.identity(_sage_const_3 )))
except:
 _st_.goboom(_sage_const_372 )
_st_.blockbegin()
try:
 x,y,z=var('x','y','z')
 f=matrix([[x**_sage_const_3 ,_sage_const_2 *x**_sage_const_2 ,_sage_const_3 *x],[_sage_const_2 *x**_sage_const_2 ,x**_sage_const_4 ,x],[_sage_const_3 *x,x,x**_sage_const_5 ]])
 par=matrix([[x**_sage_const_2 ,y*x,z*x],[y*x,y**_sage_const_2 ,y*z],[z*x,y*z,z**_sage_const_2 ]])
 q=matrix([x,y])
except:
 _st_.goboom(_sage_const_523 )
_st_.blockend()
try:
 _st_.inline(_sage_const_39 , latex(f))
except:
 _st_.goboom(_sage_const_526 )
try:
 _st_.inline(_sage_const_40 , latex(diff(f,x)))
except:
 _st_.goboom(_sage_const_532 )
try:
 _st_.inline(_sage_const_41 , latex(par))
except:
 _st_.goboom(_sage_const_539 )
try:
 _st_.inline(_sage_const_42 , latex(diff(par,x)))
except:
 _st_.goboom(_sage_const_539 )
try:
 _st_.inline(_sage_const_43 , latex(q))
except:
 _st_.goboom(_sage_const_546 )
try:
 _st_.inline(_sage_const_44 , latex(q.transpose()))
except:
 _st_.goboom(_sage_const_548 )
try:
 _st_.inline(_sage_const_45 , latex(q.transpose()))
except:
 _st_.goboom(_sage_const_572 )
try:
 _st_.inline(_sage_const_46 , latex(f))
except:
 _st_.goboom(_sage_const_598 )
try:
 _st_.inline(_sage_const_47 , latex(matrix(_sage_const_3 ,[c.integrate(x) for row in f for c in row ]) ))
except:
 _st_.goboom(_sage_const_602 )
_st_.blockbegin()
try:
 var('x1','x2','x3')
 X=matrix([x1,x2,x3])
except:
 _st_.goboom(_sage_const_618 )
_st_.blockend()
try:
 _st_.inline(_sage_const_48 , latex(a))
except:
 _st_.goboom(_sage_const_620 )
try:
 _st_.inline(_sage_const_49 , latex(X.transpose()))
except:
 _st_.goboom(_sage_const_620 )
try:
 _st_.inline(_sage_const_50 , latex(X))
except:
 _st_.goboom(_sage_const_623 )
try:
 _st_.inline(_sage_const_51 , latex(a))
except:
 _st_.goboom(_sage_const_623 )
try:
 _st_.inline(_sage_const_52 , latex(X.transpose()))
except:
 _st_.goboom(_sage_const_623 )
try:
 _st_.inline(_sage_const_53 , latex(X*a*X.transpose()))
except:
 _st_.goboom(_sage_const_624 )
_st_.blockbegin()
try:
 a=matrix([[-_sage_const_1 ,_sage_const_3 ,-_sage_const_2 ],[_sage_const_2 ,-_sage_const_4 ,_sage_const_2 ],[_sage_const_0 ,_sage_const_4 ,_sage_const_1 ]])
except:
 _st_.goboom(_sage_const_674 )
_st_.blockend()
try:
 _st_.inline(_sage_const_54 , latex(a))
except:
 _st_.goboom(_sage_const_677 )
try:
 _st_.inline(_sage_const_55 , latex(a.adjoint()))
except:
 _st_.goboom(_sage_const_702 )
try:
 _st_.inline(_sage_const_56 , latex(a.det()))
except:
 _st_.goboom(_sage_const_722 )
try:
 _st_.inline(_sage_const_57 , latex(a.inverse()))
except:
 _st_.goboom(_sage_const_726 )
try:
 _st_.inline(_sage_const_58 , latex(matrix.identity(_sage_const_3 )))
except:
 _st_.goboom(_sage_const_732 )
_st_.blockbegin()
try:
 a=matrix([[_sage_const_2 ,_sage_const_2 ,_sage_const_1 ],[_sage_const_2 ,_sage_const_1 ,_sage_const_0 ],[_sage_const_1 ,_sage_const_1 ,_sage_const_1 ]])
except:
 _st_.goboom(_sage_const_779 )
_st_.blockend()
try:
 _st_.inline(_sage_const_59 , latex(a))
except:
 _st_.goboom(_sage_const_783 )
try:
 _st_.inline(_sage_const_60 , latex(a))
except:
 _st_.goboom(_sage_const_798 )
try:
 _st_.inline(_sage_const_61 , latex(matrix.identity(_sage_const_3 )))
except:
 _st_.goboom(_sage_const_798 )
try:
 _st_.inline(_sage_const_62 , latex(a.augment(matrix.identity(_sage_const_3 ))))
except:
 _st_.goboom(_sage_const_802 )
_st_.blockbegin()
try:
 b=matrix([[_sage_const_1 ,_sage_const_1 ,_sage_const_1 /_sage_const_2 ],[_sage_const_2 ,_sage_const_1 ,_sage_const_0 ],[_sage_const_1 ,_sage_const_1 ,_sage_const_1 ]])
 b1=matrix([[_sage_const_1 /_sage_const_2 ,_sage_const_0 ,_sage_const_0 ],[_sage_const_0 ,_sage_const_1 ,_sage_const_0 ],[_sage_const_0 ,_sage_const_0 ,_sage_const_1 ]])
 c=matrix([[_sage_const_1 ,_sage_const_1 ,_sage_const_1 /_sage_const_2 ],[_sage_const_0 ,-_sage_const_1 ,-_sage_const_1 ],[_sage_const_1 ,_sage_const_1 ,_sage_const_1 ]])
 c1=matrix([[_sage_const_1 /_sage_const_2 ,_sage_const_0 ,_sage_const_0 ],[-_sage_const_1 ,_sage_const_1 ,_sage_const_0 ],[_sage_const_0 ,_sage_const_0 ,_sage_const_1 ]])
except:
 _st_.goboom(_sage_const_811 )
_st_.blockend()
try:
 _st_.inline(_sage_const_63 , latex(b.augment(b1)))
except:
 _st_.goboom(_sage_const_817 )
try:
 _st_.inline(_sage_const_64 , latex(c.augment(c1)))
except:
 _st_.goboom(_sage_const_824 )
try:
 _st_.inline(_sage_const_65 , latex(matrix([[_sage_const_1 ,_sage_const_1 ,_sage_const_1 /_sage_const_2 ,_sage_const_1 /_sage_const_2 ,_sage_const_0 ,_sage_const_0 ],[_sage_const_0 ,-_sage_const_1 ,-_sage_const_1 ,-_sage_const_1 ,_sage_const_1 ,_sage_const_0 ],[_sage_const_0 ,_sage_const_0 ,_sage_const_1 /_sage_const_2 ,-_sage_const_1 /_sage_const_2 ,_sage_const_0 ,_sage_const_1 ]])))
except:
 _st_.goboom(_sage_const_830 )
try:
 _st_.inline(_sage_const_66 , latex(matrix([[_sage_const_1 ,_sage_const_1 ,_sage_const_1 /_sage_const_2 ,_sage_const_1 /_sage_const_2 ,_sage_const_0 ,_sage_const_0 ],[_sage_const_0 ,_sage_const_1 ,_sage_const_1 ,_sage_const_1 ,-_sage_const_1 ,_sage_const_0 ],[_sage_const_0 ,_sage_const_0 ,_sage_const_1 ,-_sage_const_1 ,_sage_const_0 ,_sage_const_2 ]])))
except:
 _st_.goboom(_sage_const_836 )
try:
 _st_.inline(_sage_const_67 , latex(matrix([[_sage_const_1 ,_sage_const_1 ,_sage_const_1 /_sage_const_2 ,_sage_const_1 /_sage_const_2 ,_sage_const_0 ,_sage_const_0 ],[_sage_const_0 ,_sage_const_1 ,_sage_const_0 ,_sage_const_2 ,-_sage_const_1 ,-_sage_const_2 ],[_sage_const_0 ,_sage_const_0 ,_sage_const_1 ,-_sage_const_1 ,_sage_const_0 ,_sage_const_2 ]])))
except:
 _st_.goboom(_sage_const_842 )
try:
 _st_.inline(_sage_const_68 , latex(matrix([[_sage_const_1 ,_sage_const_1 ,_sage_const_0 ,_sage_const_1 ,_sage_const_0 ,-_sage_const_1 ],[_sage_const_0 ,_sage_const_1 ,_sage_const_0 ,_sage_const_2 ,-_sage_const_1 ,-_sage_const_2 ],[_sage_const_0 ,_sage_const_0 ,_sage_const_1 ,-_sage_const_1 ,_sage_const_0 ,_sage_const_2 ]])))
except:
 _st_.goboom(_sage_const_849 )
try:
 _st_.inline(_sage_const_69 , latex((matrix.identity(QQ,_sage_const_3 )).augment(a.inverse())))
except:
 _st_.goboom(_sage_const_855 )
try:
 _st_.inline(_sage_const_70 , latex(a.inverse()))
except:
 _st_.goboom(_sage_const_863 )
_st_.endofdoc()