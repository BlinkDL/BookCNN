#-*-coding:utf-8-*-
import random
import time
import numpy as np
import config

def apply_random_symmetry(b):
    
	# 对于每个局面...
    for i in range(0, len(b) / (config.head + 361)):

        k = i * (config.head + 361) # 找到其在数组中的偏移
        action = np.random.randint(1, 9) # 生成1-8的随机数，1代表不变

        if action==2:
            b[k+0] = 18 - b[k+0]
            tmp = b[k+2]; b[k+2] = b[k+20]; b[k+20] = tmp
            tmp = b[k+21]; b[k+21] = b[k+39]; b[k+39] = tmp
            tmp = b[k+40]; b[k+40] = b[k+58]; b[k+58] = tmp
            tmp = b[k+59]; b[k+59] = b[k+77]; b[k+77] = tmp
            tmp = b[k+78]; b[k+78] = b[k+96]; b[k+96] = tmp
            tmp = b[k+97]; b[k+97] = b[k+115]; b[k+115] = tmp
            tmp = b[k+116]; b[k+116] = b[k+134]; b[k+134] = tmp
            tmp = b[k+135]; b[k+135] = b[k+153]; b[k+153] = tmp
            tmp = b[k+154]; b[k+154] = b[k+172]; b[k+172] = tmp
            tmp = b[k+173]; b[k+173] = b[k+191]; b[k+191] = tmp
            tmp = b[k+192]; b[k+192] = b[k+210]; b[k+210] = tmp
            tmp = b[k+211]; b[k+211] = b[k+229]; b[k+229] = tmp
            tmp = b[k+230]; b[k+230] = b[k+248]; b[k+248] = tmp
            tmp = b[k+249]; b[k+249] = b[k+267]; b[k+267] = tmp
            tmp = b[k+268]; b[k+268] = b[k+286]; b[k+286] = tmp
            tmp = b[k+287]; b[k+287] = b[k+305]; b[k+305] = tmp
            tmp = b[k+306]; b[k+306] = b[k+324]; b[k+324] = tmp
            tmp = b[k+325]; b[k+325] = b[k+343]; b[k+343] = tmp
            tmp = b[k+344]; b[k+344] = b[k+362]; b[k+362] = tmp
            tmp = b[k+3]; b[k+3] = b[k+19]; b[k+19] = tmp
            tmp = b[k+22]; b[k+22] = b[k+38]; b[k+38] = tmp
            tmp = b[k+41]; b[k+41] = b[k+57]; b[k+57] = tmp
            tmp = b[k+60]; b[k+60] = b[k+76]; b[k+76] = tmp
            tmp = b[k+79]; b[k+79] = b[k+95]; b[k+95] = tmp
            tmp = b[k+98]; b[k+98] = b[k+114]; b[k+114] = tmp
            tmp = b[k+117]; b[k+117] = b[k+133]; b[k+133] = tmp
            tmp = b[k+136]; b[k+136] = b[k+152]; b[k+152] = tmp
            tmp = b[k+155]; b[k+155] = b[k+171]; b[k+171] = tmp
            tmp = b[k+174]; b[k+174] = b[k+190]; b[k+190] = tmp
            tmp = b[k+193]; b[k+193] = b[k+209]; b[k+209] = tmp
            tmp = b[k+212]; b[k+212] = b[k+228]; b[k+228] = tmp
            tmp = b[k+231]; b[k+231] = b[k+247]; b[k+247] = tmp
            tmp = b[k+250]; b[k+250] = b[k+266]; b[k+266] = tmp
            tmp = b[k+269]; b[k+269] = b[k+285]; b[k+285] = tmp
            tmp = b[k+288]; b[k+288] = b[k+304]; b[k+304] = tmp
            tmp = b[k+307]; b[k+307] = b[k+323]; b[k+323] = tmp
            tmp = b[k+326]; b[k+326] = b[k+342]; b[k+342] = tmp
            tmp = b[k+345]; b[k+345] = b[k+361]; b[k+361] = tmp
            tmp = b[k+4]; b[k+4] = b[k+18]; b[k+18] = tmp
            tmp = b[k+23]; b[k+23] = b[k+37]; b[k+37] = tmp
            tmp = b[k+42]; b[k+42] = b[k+56]; b[k+56] = tmp
            tmp = b[k+61]; b[k+61] = b[k+75]; b[k+75] = tmp
            tmp = b[k+80]; b[k+80] = b[k+94]; b[k+94] = tmp
            tmp = b[k+99]; b[k+99] = b[k+113]; b[k+113] = tmp
            tmp = b[k+118]; b[k+118] = b[k+132]; b[k+132] = tmp
            tmp = b[k+137]; b[k+137] = b[k+151]; b[k+151] = tmp
            tmp = b[k+156]; b[k+156] = b[k+170]; b[k+170] = tmp
            tmp = b[k+175]; b[k+175] = b[k+189]; b[k+189] = tmp
            tmp = b[k+194]; b[k+194] = b[k+208]; b[k+208] = tmp
            tmp = b[k+213]; b[k+213] = b[k+227]; b[k+227] = tmp
            tmp = b[k+232]; b[k+232] = b[k+246]; b[k+246] = tmp
            tmp = b[k+251]; b[k+251] = b[k+265]; b[k+265] = tmp
            tmp = b[k+270]; b[k+270] = b[k+284]; b[k+284] = tmp
            tmp = b[k+289]; b[k+289] = b[k+303]; b[k+303] = tmp
            tmp = b[k+308]; b[k+308] = b[k+322]; b[k+322] = tmp
            tmp = b[k+327]; b[k+327] = b[k+341]; b[k+341] = tmp
            tmp = b[k+346]; b[k+346] = b[k+360]; b[k+360] = tmp
            tmp = b[k+5]; b[k+5] = b[k+17]; b[k+17] = tmp
            tmp = b[k+24]; b[k+24] = b[k+36]; b[k+36] = tmp
            tmp = b[k+43]; b[k+43] = b[k+55]; b[k+55] = tmp
            tmp = b[k+62]; b[k+62] = b[k+74]; b[k+74] = tmp
            tmp = b[k+81]; b[k+81] = b[k+93]; b[k+93] = tmp
            tmp = b[k+100]; b[k+100] = b[k+112]; b[k+112] = tmp
            tmp = b[k+119]; b[k+119] = b[k+131]; b[k+131] = tmp
            tmp = b[k+138]; b[k+138] = b[k+150]; b[k+150] = tmp
            tmp = b[k+157]; b[k+157] = b[k+169]; b[k+169] = tmp
            tmp = b[k+176]; b[k+176] = b[k+188]; b[k+188] = tmp
            tmp = b[k+195]; b[k+195] = b[k+207]; b[k+207] = tmp
            tmp = b[k+214]; b[k+214] = b[k+226]; b[k+226] = tmp
            tmp = b[k+233]; b[k+233] = b[k+245]; b[k+245] = tmp
            tmp = b[k+252]; b[k+252] = b[k+264]; b[k+264] = tmp
            tmp = b[k+271]; b[k+271] = b[k+283]; b[k+283] = tmp
            tmp = b[k+290]; b[k+290] = b[k+302]; b[k+302] = tmp
            tmp = b[k+309]; b[k+309] = b[k+321]; b[k+321] = tmp
            tmp = b[k+328]; b[k+328] = b[k+340]; b[k+340] = tmp
            tmp = b[k+347]; b[k+347] = b[k+359]; b[k+359] = tmp
            tmp = b[k+6]; b[k+6] = b[k+16]; b[k+16] = tmp
            tmp = b[k+25]; b[k+25] = b[k+35]; b[k+35] = tmp
            tmp = b[k+44]; b[k+44] = b[k+54]; b[k+54] = tmp
            tmp = b[k+63]; b[k+63] = b[k+73]; b[k+73] = tmp
            tmp = b[k+82]; b[k+82] = b[k+92]; b[k+92] = tmp
            tmp = b[k+101]; b[k+101] = b[k+111]; b[k+111] = tmp
            tmp = b[k+120]; b[k+120] = b[k+130]; b[k+130] = tmp
            tmp = b[k+139]; b[k+139] = b[k+149]; b[k+149] = tmp
            tmp = b[k+158]; b[k+158] = b[k+168]; b[k+168] = tmp
            tmp = b[k+177]; b[k+177] = b[k+187]; b[k+187] = tmp
            tmp = b[k+196]; b[k+196] = b[k+206]; b[k+206] = tmp
            tmp = b[k+215]; b[k+215] = b[k+225]; b[k+225] = tmp
            tmp = b[k+234]; b[k+234] = b[k+244]; b[k+244] = tmp
            tmp = b[k+253]; b[k+253] = b[k+263]; b[k+263] = tmp
            tmp = b[k+272]; b[k+272] = b[k+282]; b[k+282] = tmp
            tmp = b[k+291]; b[k+291] = b[k+301]; b[k+301] = tmp
            tmp = b[k+310]; b[k+310] = b[k+320]; b[k+320] = tmp
            tmp = b[k+329]; b[k+329] = b[k+339]; b[k+339] = tmp
            tmp = b[k+348]; b[k+348] = b[k+358]; b[k+358] = tmp
            tmp = b[k+7]; b[k+7] = b[k+15]; b[k+15] = tmp
            tmp = b[k+26]; b[k+26] = b[k+34]; b[k+34] = tmp
            tmp = b[k+45]; b[k+45] = b[k+53]; b[k+53] = tmp
            tmp = b[k+64]; b[k+64] = b[k+72]; b[k+72] = tmp
            tmp = b[k+83]; b[k+83] = b[k+91]; b[k+91] = tmp
            tmp = b[k+102]; b[k+102] = b[k+110]; b[k+110] = tmp
            tmp = b[k+121]; b[k+121] = b[k+129]; b[k+129] = tmp
            tmp = b[k+140]; b[k+140] = b[k+148]; b[k+148] = tmp
            tmp = b[k+159]; b[k+159] = b[k+167]; b[k+167] = tmp
            tmp = b[k+178]; b[k+178] = b[k+186]; b[k+186] = tmp
            tmp = b[k+197]; b[k+197] = b[k+205]; b[k+205] = tmp
            tmp = b[k+216]; b[k+216] = b[k+224]; b[k+224] = tmp
            tmp = b[k+235]; b[k+235] = b[k+243]; b[k+243] = tmp
            tmp = b[k+254]; b[k+254] = b[k+262]; b[k+262] = tmp
            tmp = b[k+273]; b[k+273] = b[k+281]; b[k+281] = tmp
            tmp = b[k+292]; b[k+292] = b[k+300]; b[k+300] = tmp
            tmp = b[k+311]; b[k+311] = b[k+319]; b[k+319] = tmp
            tmp = b[k+330]; b[k+330] = b[k+338]; b[k+338] = tmp
            tmp = b[k+349]; b[k+349] = b[k+357]; b[k+357] = tmp
            tmp = b[k+8]; b[k+8] = b[k+14]; b[k+14] = tmp
            tmp = b[k+27]; b[k+27] = b[k+33]; b[k+33] = tmp
            tmp = b[k+46]; b[k+46] = b[k+52]; b[k+52] = tmp
            tmp = b[k+65]; b[k+65] = b[k+71]; b[k+71] = tmp
            tmp = b[k+84]; b[k+84] = b[k+90]; b[k+90] = tmp
            tmp = b[k+103]; b[k+103] = b[k+109]; b[k+109] = tmp
            tmp = b[k+122]; b[k+122] = b[k+128]; b[k+128] = tmp
            tmp = b[k+141]; b[k+141] = b[k+147]; b[k+147] = tmp
            tmp = b[k+160]; b[k+160] = b[k+166]; b[k+166] = tmp
            tmp = b[k+179]; b[k+179] = b[k+185]; b[k+185] = tmp
            tmp = b[k+198]; b[k+198] = b[k+204]; b[k+204] = tmp
            tmp = b[k+217]; b[k+217] = b[k+223]; b[k+223] = tmp
            tmp = b[k+236]; b[k+236] = b[k+242]; b[k+242] = tmp
            tmp = b[k+255]; b[k+255] = b[k+261]; b[k+261] = tmp
            tmp = b[k+274]; b[k+274] = b[k+280]; b[k+280] = tmp
            tmp = b[k+293]; b[k+293] = b[k+299]; b[k+299] = tmp
            tmp = b[k+312]; b[k+312] = b[k+318]; b[k+318] = tmp
            tmp = b[k+331]; b[k+331] = b[k+337]; b[k+337] = tmp
            tmp = b[k+350]; b[k+350] = b[k+356]; b[k+356] = tmp
            tmp = b[k+9]; b[k+9] = b[k+13]; b[k+13] = tmp
            tmp = b[k+28]; b[k+28] = b[k+32]; b[k+32] = tmp
            tmp = b[k+47]; b[k+47] = b[k+51]; b[k+51] = tmp
            tmp = b[k+66]; b[k+66] = b[k+70]; b[k+70] = tmp
            tmp = b[k+85]; b[k+85] = b[k+89]; b[k+89] = tmp
            tmp = b[k+104]; b[k+104] = b[k+108]; b[k+108] = tmp
            tmp = b[k+123]; b[k+123] = b[k+127]; b[k+127] = tmp
            tmp = b[k+142]; b[k+142] = b[k+146]; b[k+146] = tmp
            tmp = b[k+161]; b[k+161] = b[k+165]; b[k+165] = tmp
            tmp = b[k+180]; b[k+180] = b[k+184]; b[k+184] = tmp
            tmp = b[k+199]; b[k+199] = b[k+203]; b[k+203] = tmp
            tmp = b[k+218]; b[k+218] = b[k+222]; b[k+222] = tmp
            tmp = b[k+237]; b[k+237] = b[k+241]; b[k+241] = tmp
            tmp = b[k+256]; b[k+256] = b[k+260]; b[k+260] = tmp
            tmp = b[k+275]; b[k+275] = b[k+279]; b[k+279] = tmp
            tmp = b[k+294]; b[k+294] = b[k+298]; b[k+298] = tmp
            tmp = b[k+313]; b[k+313] = b[k+317]; b[k+317] = tmp
            tmp = b[k+332]; b[k+332] = b[k+336]; b[k+336] = tmp
            tmp = b[k+351]; b[k+351] = b[k+355]; b[k+355] = tmp
            tmp = b[k+10]; b[k+10] = b[k+12]; b[k+12] = tmp
            tmp = b[k+29]; b[k+29] = b[k+31]; b[k+31] = tmp
            tmp = b[k+48]; b[k+48] = b[k+50]; b[k+50] = tmp
            tmp = b[k+67]; b[k+67] = b[k+69]; b[k+69] = tmp
            tmp = b[k+86]; b[k+86] = b[k+88]; b[k+88] = tmp
            tmp = b[k+105]; b[k+105] = b[k+107]; b[k+107] = tmp
            tmp = b[k+124]; b[k+124] = b[k+126]; b[k+126] = tmp
            tmp = b[k+143]; b[k+143] = b[k+145]; b[k+145] = tmp
            tmp = b[k+162]; b[k+162] = b[k+164]; b[k+164] = tmp
            tmp = b[k+181]; b[k+181] = b[k+183]; b[k+183] = tmp
            tmp = b[k+200]; b[k+200] = b[k+202]; b[k+202] = tmp
            tmp = b[k+219]; b[k+219] = b[k+221]; b[k+221] = tmp
            tmp = b[k+238]; b[k+238] = b[k+240]; b[k+240] = tmp
            tmp = b[k+257]; b[k+257] = b[k+259]; b[k+259] = tmp
            tmp = b[k+276]; b[k+276] = b[k+278]; b[k+278] = tmp
            tmp = b[k+295]; b[k+295] = b[k+297]; b[k+297] = tmp
            tmp = b[k+314]; b[k+314] = b[k+316]; b[k+316] = tmp
            tmp = b[k+333]; b[k+333] = b[k+335]; b[k+335] = tmp
            tmp = b[k+352]; b[k+352] = b[k+354]; b[k+354] = tmp
        elif action==3:
            b[k+1] = 18 - b[k+1]
            tmp = b[k+2]; b[k+2] = b[k+344]; b[k+344] = tmp
            tmp = b[k+3]; b[k+3] = b[k+345]; b[k+345] = tmp
            tmp = b[k+4]; b[k+4] = b[k+346]; b[k+346] = tmp
            tmp = b[k+5]; b[k+5] = b[k+347]; b[k+347] = tmp
            tmp = b[k+6]; b[k+6] = b[k+348]; b[k+348] = tmp
            tmp = b[k+7]; b[k+7] = b[k+349]; b[k+349] = tmp
            tmp = b[k+8]; b[k+8] = b[k+350]; b[k+350] = tmp
            tmp = b[k+9]; b[k+9] = b[k+351]; b[k+351] = tmp
            tmp = b[k+10]; b[k+10] = b[k+352]; b[k+352] = tmp
            tmp = b[k+11]; b[k+11] = b[k+353]; b[k+353] = tmp
            tmp = b[k+12]; b[k+12] = b[k+354]; b[k+354] = tmp
            tmp = b[k+13]; b[k+13] = b[k+355]; b[k+355] = tmp
            tmp = b[k+14]; b[k+14] = b[k+356]; b[k+356] = tmp
            tmp = b[k+15]; b[k+15] = b[k+357]; b[k+357] = tmp
            tmp = b[k+16]; b[k+16] = b[k+358]; b[k+358] = tmp
            tmp = b[k+17]; b[k+17] = b[k+359]; b[k+359] = tmp
            tmp = b[k+18]; b[k+18] = b[k+360]; b[k+360] = tmp
            tmp = b[k+19]; b[k+19] = b[k+361]; b[k+361] = tmp
            tmp = b[k+20]; b[k+20] = b[k+362]; b[k+362] = tmp
            tmp = b[k+21]; b[k+21] = b[k+325]; b[k+325] = tmp
            tmp = b[k+22]; b[k+22] = b[k+326]; b[k+326] = tmp
            tmp = b[k+23]; b[k+23] = b[k+327]; b[k+327] = tmp
            tmp = b[k+24]; b[k+24] = b[k+328]; b[k+328] = tmp
            tmp = b[k+25]; b[k+25] = b[k+329]; b[k+329] = tmp
            tmp = b[k+26]; b[k+26] = b[k+330]; b[k+330] = tmp
            tmp = b[k+27]; b[k+27] = b[k+331]; b[k+331] = tmp
            tmp = b[k+28]; b[k+28] = b[k+332]; b[k+332] = tmp
            tmp = b[k+29]; b[k+29] = b[k+333]; b[k+333] = tmp
            tmp = b[k+30]; b[k+30] = b[k+334]; b[k+334] = tmp
            tmp = b[k+31]; b[k+31] = b[k+335]; b[k+335] = tmp
            tmp = b[k+32]; b[k+32] = b[k+336]; b[k+336] = tmp
            tmp = b[k+33]; b[k+33] = b[k+337]; b[k+337] = tmp
            tmp = b[k+34]; b[k+34] = b[k+338]; b[k+338] = tmp
            tmp = b[k+35]; b[k+35] = b[k+339]; b[k+339] = tmp
            tmp = b[k+36]; b[k+36] = b[k+340]; b[k+340] = tmp
            tmp = b[k+37]; b[k+37] = b[k+341]; b[k+341] = tmp
            tmp = b[k+38]; b[k+38] = b[k+342]; b[k+342] = tmp
            tmp = b[k+39]; b[k+39] = b[k+343]; b[k+343] = tmp
            tmp = b[k+40]; b[k+40] = b[k+306]; b[k+306] = tmp
            tmp = b[k+41]; b[k+41] = b[k+307]; b[k+307] = tmp
            tmp = b[k+42]; b[k+42] = b[k+308]; b[k+308] = tmp
            tmp = b[k+43]; b[k+43] = b[k+309]; b[k+309] = tmp
            tmp = b[k+44]; b[k+44] = b[k+310]; b[k+310] = tmp
            tmp = b[k+45]; b[k+45] = b[k+311]; b[k+311] = tmp
            tmp = b[k+46]; b[k+46] = b[k+312]; b[k+312] = tmp
            tmp = b[k+47]; b[k+47] = b[k+313]; b[k+313] = tmp
            tmp = b[k+48]; b[k+48] = b[k+314]; b[k+314] = tmp
            tmp = b[k+49]; b[k+49] = b[k+315]; b[k+315] = tmp
            tmp = b[k+50]; b[k+50] = b[k+316]; b[k+316] = tmp
            tmp = b[k+51]; b[k+51] = b[k+317]; b[k+317] = tmp
            tmp = b[k+52]; b[k+52] = b[k+318]; b[k+318] = tmp
            tmp = b[k+53]; b[k+53] = b[k+319]; b[k+319] = tmp
            tmp = b[k+54]; b[k+54] = b[k+320]; b[k+320] = tmp
            tmp = b[k+55]; b[k+55] = b[k+321]; b[k+321] = tmp
            tmp = b[k+56]; b[k+56] = b[k+322]; b[k+322] = tmp
            tmp = b[k+57]; b[k+57] = b[k+323]; b[k+323] = tmp
            tmp = b[k+58]; b[k+58] = b[k+324]; b[k+324] = tmp
            tmp = b[k+59]; b[k+59] = b[k+287]; b[k+287] = tmp
            tmp = b[k+60]; b[k+60] = b[k+288]; b[k+288] = tmp
            tmp = b[k+61]; b[k+61] = b[k+289]; b[k+289] = tmp
            tmp = b[k+62]; b[k+62] = b[k+290]; b[k+290] = tmp
            tmp = b[k+63]; b[k+63] = b[k+291]; b[k+291] = tmp
            tmp = b[k+64]; b[k+64] = b[k+292]; b[k+292] = tmp
            tmp = b[k+65]; b[k+65] = b[k+293]; b[k+293] = tmp
            tmp = b[k+66]; b[k+66] = b[k+294]; b[k+294] = tmp
            tmp = b[k+67]; b[k+67] = b[k+295]; b[k+295] = tmp
            tmp = b[k+68]; b[k+68] = b[k+296]; b[k+296] = tmp
            tmp = b[k+69]; b[k+69] = b[k+297]; b[k+297] = tmp
            tmp = b[k+70]; b[k+70] = b[k+298]; b[k+298] = tmp
            tmp = b[k+71]; b[k+71] = b[k+299]; b[k+299] = tmp
            tmp = b[k+72]; b[k+72] = b[k+300]; b[k+300] = tmp
            tmp = b[k+73]; b[k+73] = b[k+301]; b[k+301] = tmp
            tmp = b[k+74]; b[k+74] = b[k+302]; b[k+302] = tmp
            tmp = b[k+75]; b[k+75] = b[k+303]; b[k+303] = tmp
            tmp = b[k+76]; b[k+76] = b[k+304]; b[k+304] = tmp
            tmp = b[k+77]; b[k+77] = b[k+305]; b[k+305] = tmp
            tmp = b[k+78]; b[k+78] = b[k+268]; b[k+268] = tmp
            tmp = b[k+79]; b[k+79] = b[k+269]; b[k+269] = tmp
            tmp = b[k+80]; b[k+80] = b[k+270]; b[k+270] = tmp
            tmp = b[k+81]; b[k+81] = b[k+271]; b[k+271] = tmp
            tmp = b[k+82]; b[k+82] = b[k+272]; b[k+272] = tmp
            tmp = b[k+83]; b[k+83] = b[k+273]; b[k+273] = tmp
            tmp = b[k+84]; b[k+84] = b[k+274]; b[k+274] = tmp
            tmp = b[k+85]; b[k+85] = b[k+275]; b[k+275] = tmp
            tmp = b[k+86]; b[k+86] = b[k+276]; b[k+276] = tmp
            tmp = b[k+87]; b[k+87] = b[k+277]; b[k+277] = tmp
            tmp = b[k+88]; b[k+88] = b[k+278]; b[k+278] = tmp
            tmp = b[k+89]; b[k+89] = b[k+279]; b[k+279] = tmp
            tmp = b[k+90]; b[k+90] = b[k+280]; b[k+280] = tmp
            tmp = b[k+91]; b[k+91] = b[k+281]; b[k+281] = tmp
            tmp = b[k+92]; b[k+92] = b[k+282]; b[k+282] = tmp
            tmp = b[k+93]; b[k+93] = b[k+283]; b[k+283] = tmp
            tmp = b[k+94]; b[k+94] = b[k+284]; b[k+284] = tmp
            tmp = b[k+95]; b[k+95] = b[k+285]; b[k+285] = tmp
            tmp = b[k+96]; b[k+96] = b[k+286]; b[k+286] = tmp
            tmp = b[k+97]; b[k+97] = b[k+249]; b[k+249] = tmp
            tmp = b[k+98]; b[k+98] = b[k+250]; b[k+250] = tmp
            tmp = b[k+99]; b[k+99] = b[k+251]; b[k+251] = tmp
            tmp = b[k+100]; b[k+100] = b[k+252]; b[k+252] = tmp
            tmp = b[k+101]; b[k+101] = b[k+253]; b[k+253] = tmp
            tmp = b[k+102]; b[k+102] = b[k+254]; b[k+254] = tmp
            tmp = b[k+103]; b[k+103] = b[k+255]; b[k+255] = tmp
            tmp = b[k+104]; b[k+104] = b[k+256]; b[k+256] = tmp
            tmp = b[k+105]; b[k+105] = b[k+257]; b[k+257] = tmp
            tmp = b[k+106]; b[k+106] = b[k+258]; b[k+258] = tmp
            tmp = b[k+107]; b[k+107] = b[k+259]; b[k+259] = tmp
            tmp = b[k+108]; b[k+108] = b[k+260]; b[k+260] = tmp
            tmp = b[k+109]; b[k+109] = b[k+261]; b[k+261] = tmp
            tmp = b[k+110]; b[k+110] = b[k+262]; b[k+262] = tmp
            tmp = b[k+111]; b[k+111] = b[k+263]; b[k+263] = tmp
            tmp = b[k+112]; b[k+112] = b[k+264]; b[k+264] = tmp
            tmp = b[k+113]; b[k+113] = b[k+265]; b[k+265] = tmp
            tmp = b[k+114]; b[k+114] = b[k+266]; b[k+266] = tmp
            tmp = b[k+115]; b[k+115] = b[k+267]; b[k+267] = tmp
            tmp = b[k+116]; b[k+116] = b[k+230]; b[k+230] = tmp
            tmp = b[k+117]; b[k+117] = b[k+231]; b[k+231] = tmp
            tmp = b[k+118]; b[k+118] = b[k+232]; b[k+232] = tmp
            tmp = b[k+119]; b[k+119] = b[k+233]; b[k+233] = tmp
            tmp = b[k+120]; b[k+120] = b[k+234]; b[k+234] = tmp
            tmp = b[k+121]; b[k+121] = b[k+235]; b[k+235] = tmp
            tmp = b[k+122]; b[k+122] = b[k+236]; b[k+236] = tmp
            tmp = b[k+123]; b[k+123] = b[k+237]; b[k+237] = tmp
            tmp = b[k+124]; b[k+124] = b[k+238]; b[k+238] = tmp
            tmp = b[k+125]; b[k+125] = b[k+239]; b[k+239] = tmp
            tmp = b[k+126]; b[k+126] = b[k+240]; b[k+240] = tmp
            tmp = b[k+127]; b[k+127] = b[k+241]; b[k+241] = tmp
            tmp = b[k+128]; b[k+128] = b[k+242]; b[k+242] = tmp
            tmp = b[k+129]; b[k+129] = b[k+243]; b[k+243] = tmp
            tmp = b[k+130]; b[k+130] = b[k+244]; b[k+244] = tmp
            tmp = b[k+131]; b[k+131] = b[k+245]; b[k+245] = tmp
            tmp = b[k+132]; b[k+132] = b[k+246]; b[k+246] = tmp
            tmp = b[k+133]; b[k+133] = b[k+247]; b[k+247] = tmp
            tmp = b[k+134]; b[k+134] = b[k+248]; b[k+248] = tmp
            tmp = b[k+135]; b[k+135] = b[k+211]; b[k+211] = tmp
            tmp = b[k+136]; b[k+136] = b[k+212]; b[k+212] = tmp
            tmp = b[k+137]; b[k+137] = b[k+213]; b[k+213] = tmp
            tmp = b[k+138]; b[k+138] = b[k+214]; b[k+214] = tmp
            tmp = b[k+139]; b[k+139] = b[k+215]; b[k+215] = tmp
            tmp = b[k+140]; b[k+140] = b[k+216]; b[k+216] = tmp
            tmp = b[k+141]; b[k+141] = b[k+217]; b[k+217] = tmp
            tmp = b[k+142]; b[k+142] = b[k+218]; b[k+218] = tmp
            tmp = b[k+143]; b[k+143] = b[k+219]; b[k+219] = tmp
            tmp = b[k+144]; b[k+144] = b[k+220]; b[k+220] = tmp
            tmp = b[k+145]; b[k+145] = b[k+221]; b[k+221] = tmp
            tmp = b[k+146]; b[k+146] = b[k+222]; b[k+222] = tmp
            tmp = b[k+147]; b[k+147] = b[k+223]; b[k+223] = tmp
            tmp = b[k+148]; b[k+148] = b[k+224]; b[k+224] = tmp
            tmp = b[k+149]; b[k+149] = b[k+225]; b[k+225] = tmp
            tmp = b[k+150]; b[k+150] = b[k+226]; b[k+226] = tmp
            tmp = b[k+151]; b[k+151] = b[k+227]; b[k+227] = tmp
            tmp = b[k+152]; b[k+152] = b[k+228]; b[k+228] = tmp
            tmp = b[k+153]; b[k+153] = b[k+229]; b[k+229] = tmp
            tmp = b[k+154]; b[k+154] = b[k+192]; b[k+192] = tmp
            tmp = b[k+155]; b[k+155] = b[k+193]; b[k+193] = tmp
            tmp = b[k+156]; b[k+156] = b[k+194]; b[k+194] = tmp
            tmp = b[k+157]; b[k+157] = b[k+195]; b[k+195] = tmp
            tmp = b[k+158]; b[k+158] = b[k+196]; b[k+196] = tmp
            tmp = b[k+159]; b[k+159] = b[k+197]; b[k+197] = tmp
            tmp = b[k+160]; b[k+160] = b[k+198]; b[k+198] = tmp
            tmp = b[k+161]; b[k+161] = b[k+199]; b[k+199] = tmp
            tmp = b[k+162]; b[k+162] = b[k+200]; b[k+200] = tmp
            tmp = b[k+163]; b[k+163] = b[k+201]; b[k+201] = tmp
            tmp = b[k+164]; b[k+164] = b[k+202]; b[k+202] = tmp
            tmp = b[k+165]; b[k+165] = b[k+203]; b[k+203] = tmp
            tmp = b[k+166]; b[k+166] = b[k+204]; b[k+204] = tmp
            tmp = b[k+167]; b[k+167] = b[k+205]; b[k+205] = tmp
            tmp = b[k+168]; b[k+168] = b[k+206]; b[k+206] = tmp
            tmp = b[k+169]; b[k+169] = b[k+207]; b[k+207] = tmp
            tmp = b[k+170]; b[k+170] = b[k+208]; b[k+208] = tmp
            tmp = b[k+171]; b[k+171] = b[k+209]; b[k+209] = tmp
            tmp = b[k+172]; b[k+172] = b[k+210]; b[k+210] = tmp
        elif action==4:
            b[k+0] = 18 - b[k+0]; b[k+1] = 18 - b[k+1]
            tmp = b[k+2]; b[k+2] = b[k+362]; b[k+362] = tmp
            tmp = b[k+21]; b[k+21] = b[k+343]; b[k+343] = tmp
            tmp = b[k+40]; b[k+40] = b[k+324]; b[k+324] = tmp
            tmp = b[k+59]; b[k+59] = b[k+305]; b[k+305] = tmp
            tmp = b[k+78]; b[k+78] = b[k+286]; b[k+286] = tmp
            tmp = b[k+97]; b[k+97] = b[k+267]; b[k+267] = tmp
            tmp = b[k+116]; b[k+116] = b[k+248]; b[k+248] = tmp
            tmp = b[k+135]; b[k+135] = b[k+229]; b[k+229] = tmp
            tmp = b[k+154]; b[k+154] = b[k+210]; b[k+210] = tmp
            tmp = b[k+173]; b[k+173] = b[k+191]; b[k+191] = tmp
            tmp = b[k+192]; b[k+192] = b[k+172]; b[k+172] = tmp
            tmp = b[k+211]; b[k+211] = b[k+153]; b[k+153] = tmp
            tmp = b[k+230]; b[k+230] = b[k+134]; b[k+134] = tmp
            tmp = b[k+249]; b[k+249] = b[k+115]; b[k+115] = tmp
            tmp = b[k+268]; b[k+268] = b[k+96]; b[k+96] = tmp
            tmp = b[k+287]; b[k+287] = b[k+77]; b[k+77] = tmp
            tmp = b[k+306]; b[k+306] = b[k+58]; b[k+58] = tmp
            tmp = b[k+325]; b[k+325] = b[k+39]; b[k+39] = tmp
            tmp = b[k+344]; b[k+344] = b[k+20]; b[k+20] = tmp
            tmp = b[k+3]; b[k+3] = b[k+361]; b[k+361] = tmp
            tmp = b[k+22]; b[k+22] = b[k+342]; b[k+342] = tmp
            tmp = b[k+41]; b[k+41] = b[k+323]; b[k+323] = tmp
            tmp = b[k+60]; b[k+60] = b[k+304]; b[k+304] = tmp
            tmp = b[k+79]; b[k+79] = b[k+285]; b[k+285] = tmp
            tmp = b[k+98]; b[k+98] = b[k+266]; b[k+266] = tmp
            tmp = b[k+117]; b[k+117] = b[k+247]; b[k+247] = tmp
            tmp = b[k+136]; b[k+136] = b[k+228]; b[k+228] = tmp
            tmp = b[k+155]; b[k+155] = b[k+209]; b[k+209] = tmp
            tmp = b[k+174]; b[k+174] = b[k+190]; b[k+190] = tmp
            tmp = b[k+193]; b[k+193] = b[k+171]; b[k+171] = tmp
            tmp = b[k+212]; b[k+212] = b[k+152]; b[k+152] = tmp
            tmp = b[k+231]; b[k+231] = b[k+133]; b[k+133] = tmp
            tmp = b[k+250]; b[k+250] = b[k+114]; b[k+114] = tmp
            tmp = b[k+269]; b[k+269] = b[k+95]; b[k+95] = tmp
            tmp = b[k+288]; b[k+288] = b[k+76]; b[k+76] = tmp
            tmp = b[k+307]; b[k+307] = b[k+57]; b[k+57] = tmp
            tmp = b[k+326]; b[k+326] = b[k+38]; b[k+38] = tmp
            tmp = b[k+345]; b[k+345] = b[k+19]; b[k+19] = tmp
            tmp = b[k+4]; b[k+4] = b[k+360]; b[k+360] = tmp
            tmp = b[k+23]; b[k+23] = b[k+341]; b[k+341] = tmp
            tmp = b[k+42]; b[k+42] = b[k+322]; b[k+322] = tmp
            tmp = b[k+61]; b[k+61] = b[k+303]; b[k+303] = tmp
            tmp = b[k+80]; b[k+80] = b[k+284]; b[k+284] = tmp
            tmp = b[k+99]; b[k+99] = b[k+265]; b[k+265] = tmp
            tmp = b[k+118]; b[k+118] = b[k+246]; b[k+246] = tmp
            tmp = b[k+137]; b[k+137] = b[k+227]; b[k+227] = tmp
            tmp = b[k+156]; b[k+156] = b[k+208]; b[k+208] = tmp
            tmp = b[k+175]; b[k+175] = b[k+189]; b[k+189] = tmp
            tmp = b[k+194]; b[k+194] = b[k+170]; b[k+170] = tmp
            tmp = b[k+213]; b[k+213] = b[k+151]; b[k+151] = tmp
            tmp = b[k+232]; b[k+232] = b[k+132]; b[k+132] = tmp
            tmp = b[k+251]; b[k+251] = b[k+113]; b[k+113] = tmp
            tmp = b[k+270]; b[k+270] = b[k+94]; b[k+94] = tmp
            tmp = b[k+289]; b[k+289] = b[k+75]; b[k+75] = tmp
            tmp = b[k+308]; b[k+308] = b[k+56]; b[k+56] = tmp
            tmp = b[k+327]; b[k+327] = b[k+37]; b[k+37] = tmp
            tmp = b[k+346]; b[k+346] = b[k+18]; b[k+18] = tmp
            tmp = b[k+5]; b[k+5] = b[k+359]; b[k+359] = tmp
            tmp = b[k+24]; b[k+24] = b[k+340]; b[k+340] = tmp
            tmp = b[k+43]; b[k+43] = b[k+321]; b[k+321] = tmp
            tmp = b[k+62]; b[k+62] = b[k+302]; b[k+302] = tmp
            tmp = b[k+81]; b[k+81] = b[k+283]; b[k+283] = tmp
            tmp = b[k+100]; b[k+100] = b[k+264]; b[k+264] = tmp
            tmp = b[k+119]; b[k+119] = b[k+245]; b[k+245] = tmp
            tmp = b[k+138]; b[k+138] = b[k+226]; b[k+226] = tmp
            tmp = b[k+157]; b[k+157] = b[k+207]; b[k+207] = tmp
            tmp = b[k+176]; b[k+176] = b[k+188]; b[k+188] = tmp
            tmp = b[k+195]; b[k+195] = b[k+169]; b[k+169] = tmp
            tmp = b[k+214]; b[k+214] = b[k+150]; b[k+150] = tmp
            tmp = b[k+233]; b[k+233] = b[k+131]; b[k+131] = tmp
            tmp = b[k+252]; b[k+252] = b[k+112]; b[k+112] = tmp
            tmp = b[k+271]; b[k+271] = b[k+93]; b[k+93] = tmp
            tmp = b[k+290]; b[k+290] = b[k+74]; b[k+74] = tmp
            tmp = b[k+309]; b[k+309] = b[k+55]; b[k+55] = tmp
            tmp = b[k+328]; b[k+328] = b[k+36]; b[k+36] = tmp
            tmp = b[k+347]; b[k+347] = b[k+17]; b[k+17] = tmp
            tmp = b[k+6]; b[k+6] = b[k+358]; b[k+358] = tmp
            tmp = b[k+25]; b[k+25] = b[k+339]; b[k+339] = tmp
            tmp = b[k+44]; b[k+44] = b[k+320]; b[k+320] = tmp
            tmp = b[k+63]; b[k+63] = b[k+301]; b[k+301] = tmp
            tmp = b[k+82]; b[k+82] = b[k+282]; b[k+282] = tmp
            tmp = b[k+101]; b[k+101] = b[k+263]; b[k+263] = tmp
            tmp = b[k+120]; b[k+120] = b[k+244]; b[k+244] = tmp
            tmp = b[k+139]; b[k+139] = b[k+225]; b[k+225] = tmp
            tmp = b[k+158]; b[k+158] = b[k+206]; b[k+206] = tmp
            tmp = b[k+177]; b[k+177] = b[k+187]; b[k+187] = tmp
            tmp = b[k+196]; b[k+196] = b[k+168]; b[k+168] = tmp
            tmp = b[k+215]; b[k+215] = b[k+149]; b[k+149] = tmp
            tmp = b[k+234]; b[k+234] = b[k+130]; b[k+130] = tmp
            tmp = b[k+253]; b[k+253] = b[k+111]; b[k+111] = tmp
            tmp = b[k+272]; b[k+272] = b[k+92]; b[k+92] = tmp
            tmp = b[k+291]; b[k+291] = b[k+73]; b[k+73] = tmp
            tmp = b[k+310]; b[k+310] = b[k+54]; b[k+54] = tmp
            tmp = b[k+329]; b[k+329] = b[k+35]; b[k+35] = tmp
            tmp = b[k+348]; b[k+348] = b[k+16]; b[k+16] = tmp
            tmp = b[k+7]; b[k+7] = b[k+357]; b[k+357] = tmp
            tmp = b[k+26]; b[k+26] = b[k+338]; b[k+338] = tmp
            tmp = b[k+45]; b[k+45] = b[k+319]; b[k+319] = tmp
            tmp = b[k+64]; b[k+64] = b[k+300]; b[k+300] = tmp
            tmp = b[k+83]; b[k+83] = b[k+281]; b[k+281] = tmp
            tmp = b[k+102]; b[k+102] = b[k+262]; b[k+262] = tmp
            tmp = b[k+121]; b[k+121] = b[k+243]; b[k+243] = tmp
            tmp = b[k+140]; b[k+140] = b[k+224]; b[k+224] = tmp
            tmp = b[k+159]; b[k+159] = b[k+205]; b[k+205] = tmp
            tmp = b[k+178]; b[k+178] = b[k+186]; b[k+186] = tmp
            tmp = b[k+197]; b[k+197] = b[k+167]; b[k+167] = tmp
            tmp = b[k+216]; b[k+216] = b[k+148]; b[k+148] = tmp
            tmp = b[k+235]; b[k+235] = b[k+129]; b[k+129] = tmp
            tmp = b[k+254]; b[k+254] = b[k+110]; b[k+110] = tmp
            tmp = b[k+273]; b[k+273] = b[k+91]; b[k+91] = tmp
            tmp = b[k+292]; b[k+292] = b[k+72]; b[k+72] = tmp
            tmp = b[k+311]; b[k+311] = b[k+53]; b[k+53] = tmp
            tmp = b[k+330]; b[k+330] = b[k+34]; b[k+34] = tmp
            tmp = b[k+349]; b[k+349] = b[k+15]; b[k+15] = tmp
            tmp = b[k+8]; b[k+8] = b[k+356]; b[k+356] = tmp
            tmp = b[k+27]; b[k+27] = b[k+337]; b[k+337] = tmp
            tmp = b[k+46]; b[k+46] = b[k+318]; b[k+318] = tmp
            tmp = b[k+65]; b[k+65] = b[k+299]; b[k+299] = tmp
            tmp = b[k+84]; b[k+84] = b[k+280]; b[k+280] = tmp
            tmp = b[k+103]; b[k+103] = b[k+261]; b[k+261] = tmp
            tmp = b[k+122]; b[k+122] = b[k+242]; b[k+242] = tmp
            tmp = b[k+141]; b[k+141] = b[k+223]; b[k+223] = tmp
            tmp = b[k+160]; b[k+160] = b[k+204]; b[k+204] = tmp
            tmp = b[k+179]; b[k+179] = b[k+185]; b[k+185] = tmp
            tmp = b[k+198]; b[k+198] = b[k+166]; b[k+166] = tmp
            tmp = b[k+217]; b[k+217] = b[k+147]; b[k+147] = tmp
            tmp = b[k+236]; b[k+236] = b[k+128]; b[k+128] = tmp
            tmp = b[k+255]; b[k+255] = b[k+109]; b[k+109] = tmp
            tmp = b[k+274]; b[k+274] = b[k+90]; b[k+90] = tmp
            tmp = b[k+293]; b[k+293] = b[k+71]; b[k+71] = tmp
            tmp = b[k+312]; b[k+312] = b[k+52]; b[k+52] = tmp
            tmp = b[k+331]; b[k+331] = b[k+33]; b[k+33] = tmp
            tmp = b[k+350]; b[k+350] = b[k+14]; b[k+14] = tmp
            tmp = b[k+9]; b[k+9] = b[k+355]; b[k+355] = tmp
            tmp = b[k+28]; b[k+28] = b[k+336]; b[k+336] = tmp
            tmp = b[k+47]; b[k+47] = b[k+317]; b[k+317] = tmp
            tmp = b[k+66]; b[k+66] = b[k+298]; b[k+298] = tmp
            tmp = b[k+85]; b[k+85] = b[k+279]; b[k+279] = tmp
            tmp = b[k+104]; b[k+104] = b[k+260]; b[k+260] = tmp
            tmp = b[k+123]; b[k+123] = b[k+241]; b[k+241] = tmp
            tmp = b[k+142]; b[k+142] = b[k+222]; b[k+222] = tmp
            tmp = b[k+161]; b[k+161] = b[k+203]; b[k+203] = tmp
            tmp = b[k+180]; b[k+180] = b[k+184]; b[k+184] = tmp
            tmp = b[k+199]; b[k+199] = b[k+165]; b[k+165] = tmp
            tmp = b[k+218]; b[k+218] = b[k+146]; b[k+146] = tmp
            tmp = b[k+237]; b[k+237] = b[k+127]; b[k+127] = tmp
            tmp = b[k+256]; b[k+256] = b[k+108]; b[k+108] = tmp
            tmp = b[k+275]; b[k+275] = b[k+89]; b[k+89] = tmp
            tmp = b[k+294]; b[k+294] = b[k+70]; b[k+70] = tmp
            tmp = b[k+313]; b[k+313] = b[k+51]; b[k+51] = tmp
            tmp = b[k+332]; b[k+332] = b[k+32]; b[k+32] = tmp
            tmp = b[k+351]; b[k+351] = b[k+13]; b[k+13] = tmp
            tmp = b[k+10]; b[k+10] = b[k+354]; b[k+354] = tmp
            tmp = b[k+29]; b[k+29] = b[k+335]; b[k+335] = tmp
            tmp = b[k+48]; b[k+48] = b[k+316]; b[k+316] = tmp
            tmp = b[k+67]; b[k+67] = b[k+297]; b[k+297] = tmp
            tmp = b[k+86]; b[k+86] = b[k+278]; b[k+278] = tmp
            tmp = b[k+105]; b[k+105] = b[k+259]; b[k+259] = tmp
            tmp = b[k+124]; b[k+124] = b[k+240]; b[k+240] = tmp
            tmp = b[k+143]; b[k+143] = b[k+221]; b[k+221] = tmp
            tmp = b[k+162]; b[k+162] = b[k+202]; b[k+202] = tmp
            tmp = b[k+181]; b[k+181] = b[k+183]; b[k+183] = tmp
            tmp = b[k+200]; b[k+200] = b[k+164]; b[k+164] = tmp
            tmp = b[k+219]; b[k+219] = b[k+145]; b[k+145] = tmp
            tmp = b[k+238]; b[k+238] = b[k+126]; b[k+126] = tmp
            tmp = b[k+257]; b[k+257] = b[k+107]; b[k+107] = tmp
            tmp = b[k+276]; b[k+276] = b[k+88]; b[k+88] = tmp
            tmp = b[k+295]; b[k+295] = b[k+69]; b[k+69] = tmp
            tmp = b[k+314]; b[k+314] = b[k+50]; b[k+50] = tmp
            tmp = b[k+333]; b[k+333] = b[k+31]; b[k+31] = tmp
            tmp = b[k+352]; b[k+352] = b[k+12]; b[k+12] = tmp
            tmp = b[k+11]; b[k+11] = b[k+353]; b[k+353] = tmp
            tmp = b[k+30]; b[k+30] = b[k+334]; b[k+334] = tmp
            tmp = b[k+49]; b[k+49] = b[k+315]; b[k+315] = tmp
            tmp = b[k+68]; b[k+68] = b[k+296]; b[k+296] = tmp
            tmp = b[k+87]; b[k+87] = b[k+277]; b[k+277] = tmp
            tmp = b[k+106]; b[k+106] = b[k+258]; b[k+258] = tmp
            tmp = b[k+125]; b[k+125] = b[k+239]; b[k+239] = tmp
            tmp = b[k+144]; b[k+144] = b[k+220]; b[k+220] = tmp
            tmp = b[k+163]; b[k+163] = b[k+201]; b[k+201] = tmp
            tmp = b[k+182]; b[k+182] = b[k+182]; b[k+182] = tmp
        elif action==5:
            tmp = b[k+0]; b[k+0] = b[k+1]; b[k+1] = tmp
            tmp = b[k+3]; b[k+3] = b[k+21]; b[k+21] = tmp
            tmp = b[k+4]; b[k+4] = b[k+40]; b[k+40] = tmp
            tmp = b[k+5]; b[k+5] = b[k+59]; b[k+59] = tmp
            tmp = b[k+6]; b[k+6] = b[k+78]; b[k+78] = tmp
            tmp = b[k+7]; b[k+7] = b[k+97]; b[k+97] = tmp
            tmp = b[k+8]; b[k+8] = b[k+116]; b[k+116] = tmp
            tmp = b[k+9]; b[k+9] = b[k+135]; b[k+135] = tmp
            tmp = b[k+10]; b[k+10] = b[k+154]; b[k+154] = tmp
            tmp = b[k+11]; b[k+11] = b[k+173]; b[k+173] = tmp
            tmp = b[k+12]; b[k+12] = b[k+192]; b[k+192] = tmp
            tmp = b[k+13]; b[k+13] = b[k+211]; b[k+211] = tmp
            tmp = b[k+14]; b[k+14] = b[k+230]; b[k+230] = tmp
            tmp = b[k+15]; b[k+15] = b[k+249]; b[k+249] = tmp
            tmp = b[k+16]; b[k+16] = b[k+268]; b[k+268] = tmp
            tmp = b[k+17]; b[k+17] = b[k+287]; b[k+287] = tmp
            tmp = b[k+18]; b[k+18] = b[k+306]; b[k+306] = tmp
            tmp = b[k+19]; b[k+19] = b[k+325]; b[k+325] = tmp
            tmp = b[k+20]; b[k+20] = b[k+344]; b[k+344] = tmp
            tmp = b[k+23]; b[k+23] = b[k+41]; b[k+41] = tmp
            tmp = b[k+24]; b[k+24] = b[k+60]; b[k+60] = tmp
            tmp = b[k+25]; b[k+25] = b[k+79]; b[k+79] = tmp
            tmp = b[k+26]; b[k+26] = b[k+98]; b[k+98] = tmp
            tmp = b[k+27]; b[k+27] = b[k+117]; b[k+117] = tmp
            tmp = b[k+28]; b[k+28] = b[k+136]; b[k+136] = tmp
            tmp = b[k+29]; b[k+29] = b[k+155]; b[k+155] = tmp
            tmp = b[k+30]; b[k+30] = b[k+174]; b[k+174] = tmp
            tmp = b[k+31]; b[k+31] = b[k+193]; b[k+193] = tmp
            tmp = b[k+32]; b[k+32] = b[k+212]; b[k+212] = tmp
            tmp = b[k+33]; b[k+33] = b[k+231]; b[k+231] = tmp
            tmp = b[k+34]; b[k+34] = b[k+250]; b[k+250] = tmp
            tmp = b[k+35]; b[k+35] = b[k+269]; b[k+269] = tmp
            tmp = b[k+36]; b[k+36] = b[k+288]; b[k+288] = tmp
            tmp = b[k+37]; b[k+37] = b[k+307]; b[k+307] = tmp
            tmp = b[k+38]; b[k+38] = b[k+326]; b[k+326] = tmp
            tmp = b[k+39]; b[k+39] = b[k+345]; b[k+345] = tmp
            tmp = b[k+43]; b[k+43] = b[k+61]; b[k+61] = tmp
            tmp = b[k+44]; b[k+44] = b[k+80]; b[k+80] = tmp
            tmp = b[k+45]; b[k+45] = b[k+99]; b[k+99] = tmp
            tmp = b[k+46]; b[k+46] = b[k+118]; b[k+118] = tmp
            tmp = b[k+47]; b[k+47] = b[k+137]; b[k+137] = tmp
            tmp = b[k+48]; b[k+48] = b[k+156]; b[k+156] = tmp
            tmp = b[k+49]; b[k+49] = b[k+175]; b[k+175] = tmp
            tmp = b[k+50]; b[k+50] = b[k+194]; b[k+194] = tmp
            tmp = b[k+51]; b[k+51] = b[k+213]; b[k+213] = tmp
            tmp = b[k+52]; b[k+52] = b[k+232]; b[k+232] = tmp
            tmp = b[k+53]; b[k+53] = b[k+251]; b[k+251] = tmp
            tmp = b[k+54]; b[k+54] = b[k+270]; b[k+270] = tmp
            tmp = b[k+55]; b[k+55] = b[k+289]; b[k+289] = tmp
            tmp = b[k+56]; b[k+56] = b[k+308]; b[k+308] = tmp
            tmp = b[k+57]; b[k+57] = b[k+327]; b[k+327] = tmp
            tmp = b[k+58]; b[k+58] = b[k+346]; b[k+346] = tmp
            tmp = b[k+63]; b[k+63] = b[k+81]; b[k+81] = tmp
            tmp = b[k+64]; b[k+64] = b[k+100]; b[k+100] = tmp
            tmp = b[k+65]; b[k+65] = b[k+119]; b[k+119] = tmp
            tmp = b[k+66]; b[k+66] = b[k+138]; b[k+138] = tmp
            tmp = b[k+67]; b[k+67] = b[k+157]; b[k+157] = tmp
            tmp = b[k+68]; b[k+68] = b[k+176]; b[k+176] = tmp
            tmp = b[k+69]; b[k+69] = b[k+195]; b[k+195] = tmp
            tmp = b[k+70]; b[k+70] = b[k+214]; b[k+214] = tmp
            tmp = b[k+71]; b[k+71] = b[k+233]; b[k+233] = tmp
            tmp = b[k+72]; b[k+72] = b[k+252]; b[k+252] = tmp
            tmp = b[k+73]; b[k+73] = b[k+271]; b[k+271] = tmp
            tmp = b[k+74]; b[k+74] = b[k+290]; b[k+290] = tmp
            tmp = b[k+75]; b[k+75] = b[k+309]; b[k+309] = tmp
            tmp = b[k+76]; b[k+76] = b[k+328]; b[k+328] = tmp
            tmp = b[k+77]; b[k+77] = b[k+347]; b[k+347] = tmp
            tmp = b[k+83]; b[k+83] = b[k+101]; b[k+101] = tmp
            tmp = b[k+84]; b[k+84] = b[k+120]; b[k+120] = tmp
            tmp = b[k+85]; b[k+85] = b[k+139]; b[k+139] = tmp
            tmp = b[k+86]; b[k+86] = b[k+158]; b[k+158] = tmp
            tmp = b[k+87]; b[k+87] = b[k+177]; b[k+177] = tmp
            tmp = b[k+88]; b[k+88] = b[k+196]; b[k+196] = tmp
            tmp = b[k+89]; b[k+89] = b[k+215]; b[k+215] = tmp
            tmp = b[k+90]; b[k+90] = b[k+234]; b[k+234] = tmp
            tmp = b[k+91]; b[k+91] = b[k+253]; b[k+253] = tmp
            tmp = b[k+92]; b[k+92] = b[k+272]; b[k+272] = tmp
            tmp = b[k+93]; b[k+93] = b[k+291]; b[k+291] = tmp
            tmp = b[k+94]; b[k+94] = b[k+310]; b[k+310] = tmp
            tmp = b[k+95]; b[k+95] = b[k+329]; b[k+329] = tmp
            tmp = b[k+96]; b[k+96] = b[k+348]; b[k+348] = tmp
            tmp = b[k+103]; b[k+103] = b[k+121]; b[k+121] = tmp
            tmp = b[k+104]; b[k+104] = b[k+140]; b[k+140] = tmp
            tmp = b[k+105]; b[k+105] = b[k+159]; b[k+159] = tmp
            tmp = b[k+106]; b[k+106] = b[k+178]; b[k+178] = tmp
            tmp = b[k+107]; b[k+107] = b[k+197]; b[k+197] = tmp
            tmp = b[k+108]; b[k+108] = b[k+216]; b[k+216] = tmp
            tmp = b[k+109]; b[k+109] = b[k+235]; b[k+235] = tmp
            tmp = b[k+110]; b[k+110] = b[k+254]; b[k+254] = tmp
            tmp = b[k+111]; b[k+111] = b[k+273]; b[k+273] = tmp
            tmp = b[k+112]; b[k+112] = b[k+292]; b[k+292] = tmp
            tmp = b[k+113]; b[k+113] = b[k+311]; b[k+311] = tmp
            tmp = b[k+114]; b[k+114] = b[k+330]; b[k+330] = tmp
            tmp = b[k+115]; b[k+115] = b[k+349]; b[k+349] = tmp
            tmp = b[k+123]; b[k+123] = b[k+141]; b[k+141] = tmp
            tmp = b[k+124]; b[k+124] = b[k+160]; b[k+160] = tmp
            tmp = b[k+125]; b[k+125] = b[k+179]; b[k+179] = tmp
            tmp = b[k+126]; b[k+126] = b[k+198]; b[k+198] = tmp
            tmp = b[k+127]; b[k+127] = b[k+217]; b[k+217] = tmp
            tmp = b[k+128]; b[k+128] = b[k+236]; b[k+236] = tmp
            tmp = b[k+129]; b[k+129] = b[k+255]; b[k+255] = tmp
            tmp = b[k+130]; b[k+130] = b[k+274]; b[k+274] = tmp
            tmp = b[k+131]; b[k+131] = b[k+293]; b[k+293] = tmp
            tmp = b[k+132]; b[k+132] = b[k+312]; b[k+312] = tmp
            tmp = b[k+133]; b[k+133] = b[k+331]; b[k+331] = tmp
            tmp = b[k+134]; b[k+134] = b[k+350]; b[k+350] = tmp
            tmp = b[k+143]; b[k+143] = b[k+161]; b[k+161] = tmp
            tmp = b[k+144]; b[k+144] = b[k+180]; b[k+180] = tmp
            tmp = b[k+145]; b[k+145] = b[k+199]; b[k+199] = tmp
            tmp = b[k+146]; b[k+146] = b[k+218]; b[k+218] = tmp
            tmp = b[k+147]; b[k+147] = b[k+237]; b[k+237] = tmp
            tmp = b[k+148]; b[k+148] = b[k+256]; b[k+256] = tmp
            tmp = b[k+149]; b[k+149] = b[k+275]; b[k+275] = tmp
            tmp = b[k+150]; b[k+150] = b[k+294]; b[k+294] = tmp
            tmp = b[k+151]; b[k+151] = b[k+313]; b[k+313] = tmp
            tmp = b[k+152]; b[k+152] = b[k+332]; b[k+332] = tmp
            tmp = b[k+153]; b[k+153] = b[k+351]; b[k+351] = tmp
            tmp = b[k+163]; b[k+163] = b[k+181]; b[k+181] = tmp
            tmp = b[k+164]; b[k+164] = b[k+200]; b[k+200] = tmp
            tmp = b[k+165]; b[k+165] = b[k+219]; b[k+219] = tmp
            tmp = b[k+166]; b[k+166] = b[k+238]; b[k+238] = tmp
            tmp = b[k+167]; b[k+167] = b[k+257]; b[k+257] = tmp
            tmp = b[k+168]; b[k+168] = b[k+276]; b[k+276] = tmp
            tmp = b[k+169]; b[k+169] = b[k+295]; b[k+295] = tmp
            tmp = b[k+170]; b[k+170] = b[k+314]; b[k+314] = tmp
            tmp = b[k+171]; b[k+171] = b[k+333]; b[k+333] = tmp
            tmp = b[k+172]; b[k+172] = b[k+352]; b[k+352] = tmp
            tmp = b[k+183]; b[k+183] = b[k+201]; b[k+201] = tmp
            tmp = b[k+184]; b[k+184] = b[k+220]; b[k+220] = tmp
            tmp = b[k+185]; b[k+185] = b[k+239]; b[k+239] = tmp
            tmp = b[k+186]; b[k+186] = b[k+258]; b[k+258] = tmp
            tmp = b[k+187]; b[k+187] = b[k+277]; b[k+277] = tmp
            tmp = b[k+188]; b[k+188] = b[k+296]; b[k+296] = tmp
            tmp = b[k+189]; b[k+189] = b[k+315]; b[k+315] = tmp
            tmp = b[k+190]; b[k+190] = b[k+334]; b[k+334] = tmp
            tmp = b[k+191]; b[k+191] = b[k+353]; b[k+353] = tmp
            tmp = b[k+203]; b[k+203] = b[k+221]; b[k+221] = tmp
            tmp = b[k+204]; b[k+204] = b[k+240]; b[k+240] = tmp
            tmp = b[k+205]; b[k+205] = b[k+259]; b[k+259] = tmp
            tmp = b[k+206]; b[k+206] = b[k+278]; b[k+278] = tmp
            tmp = b[k+207]; b[k+207] = b[k+297]; b[k+297] = tmp
            tmp = b[k+208]; b[k+208] = b[k+316]; b[k+316] = tmp
            tmp = b[k+209]; b[k+209] = b[k+335]; b[k+335] = tmp
            tmp = b[k+210]; b[k+210] = b[k+354]; b[k+354] = tmp
            tmp = b[k+223]; b[k+223] = b[k+241]; b[k+241] = tmp
            tmp = b[k+224]; b[k+224] = b[k+260]; b[k+260] = tmp
            tmp = b[k+225]; b[k+225] = b[k+279]; b[k+279] = tmp
            tmp = b[k+226]; b[k+226] = b[k+298]; b[k+298] = tmp
            tmp = b[k+227]; b[k+227] = b[k+317]; b[k+317] = tmp
            tmp = b[k+228]; b[k+228] = b[k+336]; b[k+336] = tmp
            tmp = b[k+229]; b[k+229] = b[k+355]; b[k+355] = tmp
            tmp = b[k+243]; b[k+243] = b[k+261]; b[k+261] = tmp
            tmp = b[k+244]; b[k+244] = b[k+280]; b[k+280] = tmp
            tmp = b[k+245]; b[k+245] = b[k+299]; b[k+299] = tmp
            tmp = b[k+246]; b[k+246] = b[k+318]; b[k+318] = tmp
            tmp = b[k+247]; b[k+247] = b[k+337]; b[k+337] = tmp
            tmp = b[k+248]; b[k+248] = b[k+356]; b[k+356] = tmp
            tmp = b[k+263]; b[k+263] = b[k+281]; b[k+281] = tmp
            tmp = b[k+264]; b[k+264] = b[k+300]; b[k+300] = tmp
            tmp = b[k+265]; b[k+265] = b[k+319]; b[k+319] = tmp
            tmp = b[k+266]; b[k+266] = b[k+338]; b[k+338] = tmp
            tmp = b[k+267]; b[k+267] = b[k+357]; b[k+357] = tmp
            tmp = b[k+283]; b[k+283] = b[k+301]; b[k+301] = tmp
            tmp = b[k+284]; b[k+284] = b[k+320]; b[k+320] = tmp
            tmp = b[k+285]; b[k+285] = b[k+339]; b[k+339] = tmp
            tmp = b[k+286]; b[k+286] = b[k+358]; b[k+358] = tmp
            tmp = b[k+303]; b[k+303] = b[k+321]; b[k+321] = tmp
            tmp = b[k+304]; b[k+304] = b[k+340]; b[k+340] = tmp
            tmp = b[k+305]; b[k+305] = b[k+359]; b[k+359] = tmp
            tmp = b[k+323]; b[k+323] = b[k+341]; b[k+341] = tmp
            tmp = b[k+324]; b[k+324] = b[k+360]; b[k+360] = tmp
            tmp = b[k+343]; b[k+343] = b[k+361]; b[k+361] = tmp
        elif action==6:
            tmp = b[k+0]; b[k+0] = 18 - b[k+1]; b[k+1] = 18 - tmp
            tmp = b[k+2]; b[k+2] = b[k+362]; b[k+362] = tmp
            tmp = b[k+3]; b[k+3] = b[k+343]; b[k+343] = tmp
            tmp = b[k+4]; b[k+4] = b[k+324]; b[k+324] = tmp
            tmp = b[k+5]; b[k+5] = b[k+305]; b[k+305] = tmp
            tmp = b[k+6]; b[k+6] = b[k+286]; b[k+286] = tmp
            tmp = b[k+7]; b[k+7] = b[k+267]; b[k+267] = tmp
            tmp = b[k+8]; b[k+8] = b[k+248]; b[k+248] = tmp
            tmp = b[k+9]; b[k+9] = b[k+229]; b[k+229] = tmp
            tmp = b[k+10]; b[k+10] = b[k+210]; b[k+210] = tmp
            tmp = b[k+11]; b[k+11] = b[k+191]; b[k+191] = tmp
            tmp = b[k+12]; b[k+12] = b[k+172]; b[k+172] = tmp
            tmp = b[k+13]; b[k+13] = b[k+153]; b[k+153] = tmp
            tmp = b[k+14]; b[k+14] = b[k+134]; b[k+134] = tmp
            tmp = b[k+15]; b[k+15] = b[k+115]; b[k+115] = tmp
            tmp = b[k+16]; b[k+16] = b[k+96]; b[k+96] = tmp
            tmp = b[k+17]; b[k+17] = b[k+77]; b[k+77] = tmp
            tmp = b[k+18]; b[k+18] = b[k+58]; b[k+58] = tmp
            tmp = b[k+19]; b[k+19] = b[k+39]; b[k+39] = tmp
            tmp = b[k+21]; b[k+21] = b[k+361]; b[k+361] = tmp
            tmp = b[k+22]; b[k+22] = b[k+342]; b[k+342] = tmp
            tmp = b[k+23]; b[k+23] = b[k+323]; b[k+323] = tmp
            tmp = b[k+24]; b[k+24] = b[k+304]; b[k+304] = tmp
            tmp = b[k+25]; b[k+25] = b[k+285]; b[k+285] = tmp
            tmp = b[k+26]; b[k+26] = b[k+266]; b[k+266] = tmp
            tmp = b[k+27]; b[k+27] = b[k+247]; b[k+247] = tmp
            tmp = b[k+28]; b[k+28] = b[k+228]; b[k+228] = tmp
            tmp = b[k+29]; b[k+29] = b[k+209]; b[k+209] = tmp
            tmp = b[k+30]; b[k+30] = b[k+190]; b[k+190] = tmp
            tmp = b[k+31]; b[k+31] = b[k+171]; b[k+171] = tmp
            tmp = b[k+32]; b[k+32] = b[k+152]; b[k+152] = tmp
            tmp = b[k+33]; b[k+33] = b[k+133]; b[k+133] = tmp
            tmp = b[k+34]; b[k+34] = b[k+114]; b[k+114] = tmp
            tmp = b[k+35]; b[k+35] = b[k+95]; b[k+95] = tmp
            tmp = b[k+36]; b[k+36] = b[k+76]; b[k+76] = tmp
            tmp = b[k+37]; b[k+37] = b[k+57]; b[k+57] = tmp
            tmp = b[k+40]; b[k+40] = b[k+360]; b[k+360] = tmp
            tmp = b[k+41]; b[k+41] = b[k+341]; b[k+341] = tmp
            tmp = b[k+42]; b[k+42] = b[k+322]; b[k+322] = tmp
            tmp = b[k+43]; b[k+43] = b[k+303]; b[k+303] = tmp
            tmp = b[k+44]; b[k+44] = b[k+284]; b[k+284] = tmp
            tmp = b[k+45]; b[k+45] = b[k+265]; b[k+265] = tmp
            tmp = b[k+46]; b[k+46] = b[k+246]; b[k+246] = tmp
            tmp = b[k+47]; b[k+47] = b[k+227]; b[k+227] = tmp
            tmp = b[k+48]; b[k+48] = b[k+208]; b[k+208] = tmp
            tmp = b[k+49]; b[k+49] = b[k+189]; b[k+189] = tmp
            tmp = b[k+50]; b[k+50] = b[k+170]; b[k+170] = tmp
            tmp = b[k+51]; b[k+51] = b[k+151]; b[k+151] = tmp
            tmp = b[k+52]; b[k+52] = b[k+132]; b[k+132] = tmp
            tmp = b[k+53]; b[k+53] = b[k+113]; b[k+113] = tmp
            tmp = b[k+54]; b[k+54] = b[k+94]; b[k+94] = tmp
            tmp = b[k+55]; b[k+55] = b[k+75]; b[k+75] = tmp
            tmp = b[k+59]; b[k+59] = b[k+359]; b[k+359] = tmp
            tmp = b[k+60]; b[k+60] = b[k+340]; b[k+340] = tmp
            tmp = b[k+61]; b[k+61] = b[k+321]; b[k+321] = tmp
            tmp = b[k+62]; b[k+62] = b[k+302]; b[k+302] = tmp
            tmp = b[k+63]; b[k+63] = b[k+283]; b[k+283] = tmp
            tmp = b[k+64]; b[k+64] = b[k+264]; b[k+264] = tmp
            tmp = b[k+65]; b[k+65] = b[k+245]; b[k+245] = tmp
            tmp = b[k+66]; b[k+66] = b[k+226]; b[k+226] = tmp
            tmp = b[k+67]; b[k+67] = b[k+207]; b[k+207] = tmp
            tmp = b[k+68]; b[k+68] = b[k+188]; b[k+188] = tmp
            tmp = b[k+69]; b[k+69] = b[k+169]; b[k+169] = tmp
            tmp = b[k+70]; b[k+70] = b[k+150]; b[k+150] = tmp
            tmp = b[k+71]; b[k+71] = b[k+131]; b[k+131] = tmp
            tmp = b[k+72]; b[k+72] = b[k+112]; b[k+112] = tmp
            tmp = b[k+73]; b[k+73] = b[k+93]; b[k+93] = tmp
            tmp = b[k+78]; b[k+78] = b[k+358]; b[k+358] = tmp
            tmp = b[k+79]; b[k+79] = b[k+339]; b[k+339] = tmp
            tmp = b[k+80]; b[k+80] = b[k+320]; b[k+320] = tmp
            tmp = b[k+81]; b[k+81] = b[k+301]; b[k+301] = tmp
            tmp = b[k+82]; b[k+82] = b[k+282]; b[k+282] = tmp
            tmp = b[k+83]; b[k+83] = b[k+263]; b[k+263] = tmp
            tmp = b[k+84]; b[k+84] = b[k+244]; b[k+244] = tmp
            tmp = b[k+85]; b[k+85] = b[k+225]; b[k+225] = tmp
            tmp = b[k+86]; b[k+86] = b[k+206]; b[k+206] = tmp
            tmp = b[k+87]; b[k+87] = b[k+187]; b[k+187] = tmp
            tmp = b[k+88]; b[k+88] = b[k+168]; b[k+168] = tmp
            tmp = b[k+89]; b[k+89] = b[k+149]; b[k+149] = tmp
            tmp = b[k+90]; b[k+90] = b[k+130]; b[k+130] = tmp
            tmp = b[k+91]; b[k+91] = b[k+111]; b[k+111] = tmp
            tmp = b[k+97]; b[k+97] = b[k+357]; b[k+357] = tmp
            tmp = b[k+98]; b[k+98] = b[k+338]; b[k+338] = tmp
            tmp = b[k+99]; b[k+99] = b[k+319]; b[k+319] = tmp
            tmp = b[k+100]; b[k+100] = b[k+300]; b[k+300] = tmp
            tmp = b[k+101]; b[k+101] = b[k+281]; b[k+281] = tmp
            tmp = b[k+102]; b[k+102] = b[k+262]; b[k+262] = tmp
            tmp = b[k+103]; b[k+103] = b[k+243]; b[k+243] = tmp
            tmp = b[k+104]; b[k+104] = b[k+224]; b[k+224] = tmp
            tmp = b[k+105]; b[k+105] = b[k+205]; b[k+205] = tmp
            tmp = b[k+106]; b[k+106] = b[k+186]; b[k+186] = tmp
            tmp = b[k+107]; b[k+107] = b[k+167]; b[k+167] = tmp
            tmp = b[k+108]; b[k+108] = b[k+148]; b[k+148] = tmp
            tmp = b[k+109]; b[k+109] = b[k+129]; b[k+129] = tmp
            tmp = b[k+116]; b[k+116] = b[k+356]; b[k+356] = tmp
            tmp = b[k+117]; b[k+117] = b[k+337]; b[k+337] = tmp
            tmp = b[k+118]; b[k+118] = b[k+318]; b[k+318] = tmp
            tmp = b[k+119]; b[k+119] = b[k+299]; b[k+299] = tmp
            tmp = b[k+120]; b[k+120] = b[k+280]; b[k+280] = tmp
            tmp = b[k+121]; b[k+121] = b[k+261]; b[k+261] = tmp
            tmp = b[k+122]; b[k+122] = b[k+242]; b[k+242] = tmp
            tmp = b[k+123]; b[k+123] = b[k+223]; b[k+223] = tmp
            tmp = b[k+124]; b[k+124] = b[k+204]; b[k+204] = tmp
            tmp = b[k+125]; b[k+125] = b[k+185]; b[k+185] = tmp
            tmp = b[k+126]; b[k+126] = b[k+166]; b[k+166] = tmp
            tmp = b[k+127]; b[k+127] = b[k+147]; b[k+147] = tmp
            tmp = b[k+135]; b[k+135] = b[k+355]; b[k+355] = tmp
            tmp = b[k+136]; b[k+136] = b[k+336]; b[k+336] = tmp
            tmp = b[k+137]; b[k+137] = b[k+317]; b[k+317] = tmp
            tmp = b[k+138]; b[k+138] = b[k+298]; b[k+298] = tmp
            tmp = b[k+139]; b[k+139] = b[k+279]; b[k+279] = tmp
            tmp = b[k+140]; b[k+140] = b[k+260]; b[k+260] = tmp
            tmp = b[k+141]; b[k+141] = b[k+241]; b[k+241] = tmp
            tmp = b[k+142]; b[k+142] = b[k+222]; b[k+222] = tmp
            tmp = b[k+143]; b[k+143] = b[k+203]; b[k+203] = tmp
            tmp = b[k+144]; b[k+144] = b[k+184]; b[k+184] = tmp
            tmp = b[k+145]; b[k+145] = b[k+165]; b[k+165] = tmp
            tmp = b[k+154]; b[k+154] = b[k+354]; b[k+354] = tmp
            tmp = b[k+155]; b[k+155] = b[k+335]; b[k+335] = tmp
            tmp = b[k+156]; b[k+156] = b[k+316]; b[k+316] = tmp
            tmp = b[k+157]; b[k+157] = b[k+297]; b[k+297] = tmp
            tmp = b[k+158]; b[k+158] = b[k+278]; b[k+278] = tmp
            tmp = b[k+159]; b[k+159] = b[k+259]; b[k+259] = tmp
            tmp = b[k+160]; b[k+160] = b[k+240]; b[k+240] = tmp
            tmp = b[k+161]; b[k+161] = b[k+221]; b[k+221] = tmp
            tmp = b[k+162]; b[k+162] = b[k+202]; b[k+202] = tmp
            tmp = b[k+163]; b[k+163] = b[k+183]; b[k+183] = tmp
            tmp = b[k+173]; b[k+173] = b[k+353]; b[k+353] = tmp
            tmp = b[k+174]; b[k+174] = b[k+334]; b[k+334] = tmp
            tmp = b[k+175]; b[k+175] = b[k+315]; b[k+315] = tmp
            tmp = b[k+176]; b[k+176] = b[k+296]; b[k+296] = tmp
            tmp = b[k+177]; b[k+177] = b[k+277]; b[k+277] = tmp
            tmp = b[k+178]; b[k+178] = b[k+258]; b[k+258] = tmp
            tmp = b[k+179]; b[k+179] = b[k+239]; b[k+239] = tmp
            tmp = b[k+180]; b[k+180] = b[k+220]; b[k+220] = tmp
            tmp = b[k+181]; b[k+181] = b[k+201]; b[k+201] = tmp
            tmp = b[k+192]; b[k+192] = b[k+352]; b[k+352] = tmp
            tmp = b[k+193]; b[k+193] = b[k+333]; b[k+333] = tmp
            tmp = b[k+194]; b[k+194] = b[k+314]; b[k+314] = tmp
            tmp = b[k+195]; b[k+195] = b[k+295]; b[k+295] = tmp
            tmp = b[k+196]; b[k+196] = b[k+276]; b[k+276] = tmp
            tmp = b[k+197]; b[k+197] = b[k+257]; b[k+257] = tmp
            tmp = b[k+198]; b[k+198] = b[k+238]; b[k+238] = tmp
            tmp = b[k+199]; b[k+199] = b[k+219]; b[k+219] = tmp
            tmp = b[k+211]; b[k+211] = b[k+351]; b[k+351] = tmp
            tmp = b[k+212]; b[k+212] = b[k+332]; b[k+332] = tmp
            tmp = b[k+213]; b[k+213] = b[k+313]; b[k+313] = tmp
            tmp = b[k+214]; b[k+214] = b[k+294]; b[k+294] = tmp
            tmp = b[k+215]; b[k+215] = b[k+275]; b[k+275] = tmp
            tmp = b[k+216]; b[k+216] = b[k+256]; b[k+256] = tmp
            tmp = b[k+217]; b[k+217] = b[k+237]; b[k+237] = tmp
            tmp = b[k+230]; b[k+230] = b[k+350]; b[k+350] = tmp
            tmp = b[k+231]; b[k+231] = b[k+331]; b[k+331] = tmp
            tmp = b[k+232]; b[k+232] = b[k+312]; b[k+312] = tmp
            tmp = b[k+233]; b[k+233] = b[k+293]; b[k+293] = tmp
            tmp = b[k+234]; b[k+234] = b[k+274]; b[k+274] = tmp
            tmp = b[k+235]; b[k+235] = b[k+255]; b[k+255] = tmp
            tmp = b[k+249]; b[k+249] = b[k+349]; b[k+349] = tmp
            tmp = b[k+250]; b[k+250] = b[k+330]; b[k+330] = tmp
            tmp = b[k+251]; b[k+251] = b[k+311]; b[k+311] = tmp
            tmp = b[k+252]; b[k+252] = b[k+292]; b[k+292] = tmp
            tmp = b[k+253]; b[k+253] = b[k+273]; b[k+273] = tmp
            tmp = b[k+268]; b[k+268] = b[k+348]; b[k+348] = tmp
            tmp = b[k+269]; b[k+269] = b[k+329]; b[k+329] = tmp
            tmp = b[k+270]; b[k+270] = b[k+310]; b[k+310] = tmp
            tmp = b[k+271]; b[k+271] = b[k+291]; b[k+291] = tmp
            tmp = b[k+287]; b[k+287] = b[k+347]; b[k+347] = tmp
            tmp = b[k+288]; b[k+288] = b[k+328]; b[k+328] = tmp
            tmp = b[k+289]; b[k+289] = b[k+309]; b[k+309] = tmp
            tmp = b[k+306]; b[k+306] = b[k+346]; b[k+346] = tmp
            tmp = b[k+307]; b[k+307] = b[k+327]; b[k+327] = tmp
            tmp = b[k+325]; b[k+325] = b[k+345]; b[k+345] = tmp
        elif action==7:
            tmp = b[k+0]; b[k+0] = 18 - b[k+1]; b[k+1] = tmp
            tmp = b[k+2]; b[k+2] = b[k+344]; b[k+344] = b[k+362]; b[k+362] = b[k+20]; b[k+20] = tmp
            tmp = b[k+21]; b[k+21] = b[k+345]; b[k+345] = b[k+343]; b[k+343] = b[k+19]; b[k+19] = tmp
            tmp = b[k+40]; b[k+40] = b[k+346]; b[k+346] = b[k+324]; b[k+324] = b[k+18]; b[k+18] = tmp
            tmp = b[k+59]; b[k+59] = b[k+347]; b[k+347] = b[k+305]; b[k+305] = b[k+17]; b[k+17] = tmp
            tmp = b[k+78]; b[k+78] = b[k+348]; b[k+348] = b[k+286]; b[k+286] = b[k+16]; b[k+16] = tmp
            tmp = b[k+97]; b[k+97] = b[k+349]; b[k+349] = b[k+267]; b[k+267] = b[k+15]; b[k+15] = tmp
            tmp = b[k+116]; b[k+116] = b[k+350]; b[k+350] = b[k+248]; b[k+248] = b[k+14]; b[k+14] = tmp
            tmp = b[k+135]; b[k+135] = b[k+351]; b[k+351] = b[k+229]; b[k+229] = b[k+13]; b[k+13] = tmp
            tmp = b[k+154]; b[k+154] = b[k+352]; b[k+352] = b[k+210]; b[k+210] = b[k+12]; b[k+12] = tmp
            tmp = b[k+173]; b[k+173] = b[k+353]; b[k+353] = b[k+191]; b[k+191] = b[k+11]; b[k+11] = tmp
            tmp = b[k+192]; b[k+192] = b[k+354]; b[k+354] = b[k+172]; b[k+172] = b[k+10]; b[k+10] = tmp
            tmp = b[k+211]; b[k+211] = b[k+355]; b[k+355] = b[k+153]; b[k+153] = b[k+9]; b[k+9] = tmp
            tmp = b[k+230]; b[k+230] = b[k+356]; b[k+356] = b[k+134]; b[k+134] = b[k+8]; b[k+8] = tmp
            tmp = b[k+249]; b[k+249] = b[k+357]; b[k+357] = b[k+115]; b[k+115] = b[k+7]; b[k+7] = tmp
            tmp = b[k+268]; b[k+268] = b[k+358]; b[k+358] = b[k+96]; b[k+96] = b[k+6]; b[k+6] = tmp
            tmp = b[k+287]; b[k+287] = b[k+359]; b[k+359] = b[k+77]; b[k+77] = b[k+5]; b[k+5] = tmp
            tmp = b[k+306]; b[k+306] = b[k+360]; b[k+360] = b[k+58]; b[k+58] = b[k+4]; b[k+4] = tmp
            tmp = b[k+325]; b[k+325] = b[k+361]; b[k+361] = b[k+39]; b[k+39] = b[k+3]; b[k+3] = tmp
            tmp = b[k+22]; b[k+22] = b[k+326]; b[k+326] = b[k+342]; b[k+342] = b[k+38]; b[k+38] = tmp
            tmp = b[k+41]; b[k+41] = b[k+327]; b[k+327] = b[k+323]; b[k+323] = b[k+37]; b[k+37] = tmp
            tmp = b[k+60]; b[k+60] = b[k+328]; b[k+328] = b[k+304]; b[k+304] = b[k+36]; b[k+36] = tmp
            tmp = b[k+79]; b[k+79] = b[k+329]; b[k+329] = b[k+285]; b[k+285] = b[k+35]; b[k+35] = tmp
            tmp = b[k+98]; b[k+98] = b[k+330]; b[k+330] = b[k+266]; b[k+266] = b[k+34]; b[k+34] = tmp
            tmp = b[k+117]; b[k+117] = b[k+331]; b[k+331] = b[k+247]; b[k+247] = b[k+33]; b[k+33] = tmp
            tmp = b[k+136]; b[k+136] = b[k+332]; b[k+332] = b[k+228]; b[k+228] = b[k+32]; b[k+32] = tmp
            tmp = b[k+155]; b[k+155] = b[k+333]; b[k+333] = b[k+209]; b[k+209] = b[k+31]; b[k+31] = tmp
            tmp = b[k+174]; b[k+174] = b[k+334]; b[k+334] = b[k+190]; b[k+190] = b[k+30]; b[k+30] = tmp
            tmp = b[k+193]; b[k+193] = b[k+335]; b[k+335] = b[k+171]; b[k+171] = b[k+29]; b[k+29] = tmp
            tmp = b[k+212]; b[k+212] = b[k+336]; b[k+336] = b[k+152]; b[k+152] = b[k+28]; b[k+28] = tmp
            tmp = b[k+231]; b[k+231] = b[k+337]; b[k+337] = b[k+133]; b[k+133] = b[k+27]; b[k+27] = tmp
            tmp = b[k+250]; b[k+250] = b[k+338]; b[k+338] = b[k+114]; b[k+114] = b[k+26]; b[k+26] = tmp
            tmp = b[k+269]; b[k+269] = b[k+339]; b[k+339] = b[k+95]; b[k+95] = b[k+25]; b[k+25] = tmp
            tmp = b[k+288]; b[k+288] = b[k+340]; b[k+340] = b[k+76]; b[k+76] = b[k+24]; b[k+24] = tmp
            tmp = b[k+307]; b[k+307] = b[k+341]; b[k+341] = b[k+57]; b[k+57] = b[k+23]; b[k+23] = tmp
            tmp = b[k+42]; b[k+42] = b[k+308]; b[k+308] = b[k+322]; b[k+322] = b[k+56]; b[k+56] = tmp
            tmp = b[k+61]; b[k+61] = b[k+309]; b[k+309] = b[k+303]; b[k+303] = b[k+55]; b[k+55] = tmp
            tmp = b[k+80]; b[k+80] = b[k+310]; b[k+310] = b[k+284]; b[k+284] = b[k+54]; b[k+54] = tmp
            tmp = b[k+99]; b[k+99] = b[k+311]; b[k+311] = b[k+265]; b[k+265] = b[k+53]; b[k+53] = tmp
            tmp = b[k+118]; b[k+118] = b[k+312]; b[k+312] = b[k+246]; b[k+246] = b[k+52]; b[k+52] = tmp
            tmp = b[k+137]; b[k+137] = b[k+313]; b[k+313] = b[k+227]; b[k+227] = b[k+51]; b[k+51] = tmp
            tmp = b[k+156]; b[k+156] = b[k+314]; b[k+314] = b[k+208]; b[k+208] = b[k+50]; b[k+50] = tmp
            tmp = b[k+175]; b[k+175] = b[k+315]; b[k+315] = b[k+189]; b[k+189] = b[k+49]; b[k+49] = tmp
            tmp = b[k+194]; b[k+194] = b[k+316]; b[k+316] = b[k+170]; b[k+170] = b[k+48]; b[k+48] = tmp
            tmp = b[k+213]; b[k+213] = b[k+317]; b[k+317] = b[k+151]; b[k+151] = b[k+47]; b[k+47] = tmp
            tmp = b[k+232]; b[k+232] = b[k+318]; b[k+318] = b[k+132]; b[k+132] = b[k+46]; b[k+46] = tmp
            tmp = b[k+251]; b[k+251] = b[k+319]; b[k+319] = b[k+113]; b[k+113] = b[k+45]; b[k+45] = tmp
            tmp = b[k+270]; b[k+270] = b[k+320]; b[k+320] = b[k+94]; b[k+94] = b[k+44]; b[k+44] = tmp
            tmp = b[k+289]; b[k+289] = b[k+321]; b[k+321] = b[k+75]; b[k+75] = b[k+43]; b[k+43] = tmp
            tmp = b[k+62]; b[k+62] = b[k+290]; b[k+290] = b[k+302]; b[k+302] = b[k+74]; b[k+74] = tmp
            tmp = b[k+81]; b[k+81] = b[k+291]; b[k+291] = b[k+283]; b[k+283] = b[k+73]; b[k+73] = tmp
            tmp = b[k+100]; b[k+100] = b[k+292]; b[k+292] = b[k+264]; b[k+264] = b[k+72]; b[k+72] = tmp
            tmp = b[k+119]; b[k+119] = b[k+293]; b[k+293] = b[k+245]; b[k+245] = b[k+71]; b[k+71] = tmp
            tmp = b[k+138]; b[k+138] = b[k+294]; b[k+294] = b[k+226]; b[k+226] = b[k+70]; b[k+70] = tmp
            tmp = b[k+157]; b[k+157] = b[k+295]; b[k+295] = b[k+207]; b[k+207] = b[k+69]; b[k+69] = tmp
            tmp = b[k+176]; b[k+176] = b[k+296]; b[k+296] = b[k+188]; b[k+188] = b[k+68]; b[k+68] = tmp
            tmp = b[k+195]; b[k+195] = b[k+297]; b[k+297] = b[k+169]; b[k+169] = b[k+67]; b[k+67] = tmp
            tmp = b[k+214]; b[k+214] = b[k+298]; b[k+298] = b[k+150]; b[k+150] = b[k+66]; b[k+66] = tmp
            tmp = b[k+233]; b[k+233] = b[k+299]; b[k+299] = b[k+131]; b[k+131] = b[k+65]; b[k+65] = tmp
            tmp = b[k+252]; b[k+252] = b[k+300]; b[k+300] = b[k+112]; b[k+112] = b[k+64]; b[k+64] = tmp
            tmp = b[k+271]; b[k+271] = b[k+301]; b[k+301] = b[k+93]; b[k+93] = b[k+63]; b[k+63] = tmp
            tmp = b[k+82]; b[k+82] = b[k+272]; b[k+272] = b[k+282]; b[k+282] = b[k+92]; b[k+92] = tmp
            tmp = b[k+101]; b[k+101] = b[k+273]; b[k+273] = b[k+263]; b[k+263] = b[k+91]; b[k+91] = tmp
            tmp = b[k+120]; b[k+120] = b[k+274]; b[k+274] = b[k+244]; b[k+244] = b[k+90]; b[k+90] = tmp
            tmp = b[k+139]; b[k+139] = b[k+275]; b[k+275] = b[k+225]; b[k+225] = b[k+89]; b[k+89] = tmp
            tmp = b[k+158]; b[k+158] = b[k+276]; b[k+276] = b[k+206]; b[k+206] = b[k+88]; b[k+88] = tmp
            tmp = b[k+177]; b[k+177] = b[k+277]; b[k+277] = b[k+187]; b[k+187] = b[k+87]; b[k+87] = tmp
            tmp = b[k+196]; b[k+196] = b[k+278]; b[k+278] = b[k+168]; b[k+168] = b[k+86]; b[k+86] = tmp
            tmp = b[k+215]; b[k+215] = b[k+279]; b[k+279] = b[k+149]; b[k+149] = b[k+85]; b[k+85] = tmp
            tmp = b[k+234]; b[k+234] = b[k+280]; b[k+280] = b[k+130]; b[k+130] = b[k+84]; b[k+84] = tmp
            tmp = b[k+253]; b[k+253] = b[k+281]; b[k+281] = b[k+111]; b[k+111] = b[k+83]; b[k+83] = tmp
            tmp = b[k+102]; b[k+102] = b[k+254]; b[k+254] = b[k+262]; b[k+262] = b[k+110]; b[k+110] = tmp
            tmp = b[k+121]; b[k+121] = b[k+255]; b[k+255] = b[k+243]; b[k+243] = b[k+109]; b[k+109] = tmp
            tmp = b[k+140]; b[k+140] = b[k+256]; b[k+256] = b[k+224]; b[k+224] = b[k+108]; b[k+108] = tmp
            tmp = b[k+159]; b[k+159] = b[k+257]; b[k+257] = b[k+205]; b[k+205] = b[k+107]; b[k+107] = tmp
            tmp = b[k+178]; b[k+178] = b[k+258]; b[k+258] = b[k+186]; b[k+186] = b[k+106]; b[k+106] = tmp
            tmp = b[k+197]; b[k+197] = b[k+259]; b[k+259] = b[k+167]; b[k+167] = b[k+105]; b[k+105] = tmp
            tmp = b[k+216]; b[k+216] = b[k+260]; b[k+260] = b[k+148]; b[k+148] = b[k+104]; b[k+104] = tmp
            tmp = b[k+235]; b[k+235] = b[k+261]; b[k+261] = b[k+129]; b[k+129] = b[k+103]; b[k+103] = tmp
            tmp = b[k+122]; b[k+122] = b[k+236]; b[k+236] = b[k+242]; b[k+242] = b[k+128]; b[k+128] = tmp
            tmp = b[k+141]; b[k+141] = b[k+237]; b[k+237] = b[k+223]; b[k+223] = b[k+127]; b[k+127] = tmp
            tmp = b[k+160]; b[k+160] = b[k+238]; b[k+238] = b[k+204]; b[k+204] = b[k+126]; b[k+126] = tmp
            tmp = b[k+179]; b[k+179] = b[k+239]; b[k+239] = b[k+185]; b[k+185] = b[k+125]; b[k+125] = tmp
            tmp = b[k+198]; b[k+198] = b[k+240]; b[k+240] = b[k+166]; b[k+166] = b[k+124]; b[k+124] = tmp
            tmp = b[k+217]; b[k+217] = b[k+241]; b[k+241] = b[k+147]; b[k+147] = b[k+123]; b[k+123] = tmp
            tmp = b[k+142]; b[k+142] = b[k+218]; b[k+218] = b[k+222]; b[k+222] = b[k+146]; b[k+146] = tmp
            tmp = b[k+161]; b[k+161] = b[k+219]; b[k+219] = b[k+203]; b[k+203] = b[k+145]; b[k+145] = tmp
            tmp = b[k+180]; b[k+180] = b[k+220]; b[k+220] = b[k+184]; b[k+184] = b[k+144]; b[k+144] = tmp
            tmp = b[k+199]; b[k+199] = b[k+221]; b[k+221] = b[k+165]; b[k+165] = b[k+143]; b[k+143] = tmp
            tmp = b[k+162]; b[k+162] = b[k+200]; b[k+200] = b[k+202]; b[k+202] = b[k+164]; b[k+164] = tmp
            tmp = b[k+181]; b[k+181] = b[k+201]; b[k+201] = b[k+183]; b[k+183] = b[k+163]; b[k+163] = tmp
        elif action==8:
            tmp = b[k+0]; b[k+0] = b[k+1]; b[k+1] = 18 - tmp
            tmp = b[k+2]; b[k+2] = b[k+20]; b[k+20] = b[k+362]; b[k+362] = b[k+344]; b[k+344] = tmp
            tmp = b[k+21]; b[k+21] = b[k+19]; b[k+19] = b[k+343]; b[k+343] = b[k+345]; b[k+345] = tmp
            tmp = b[k+40]; b[k+40] = b[k+18]; b[k+18] = b[k+324]; b[k+324] = b[k+346]; b[k+346] = tmp
            tmp = b[k+59]; b[k+59] = b[k+17]; b[k+17] = b[k+305]; b[k+305] = b[k+347]; b[k+347] = tmp
            tmp = b[k+78]; b[k+78] = b[k+16]; b[k+16] = b[k+286]; b[k+286] = b[k+348]; b[k+348] = tmp
            tmp = b[k+97]; b[k+97] = b[k+15]; b[k+15] = b[k+267]; b[k+267] = b[k+349]; b[k+349] = tmp
            tmp = b[k+116]; b[k+116] = b[k+14]; b[k+14] = b[k+248]; b[k+248] = b[k+350]; b[k+350] = tmp
            tmp = b[k+135]; b[k+135] = b[k+13]; b[k+13] = b[k+229]; b[k+229] = b[k+351]; b[k+351] = tmp
            tmp = b[k+154]; b[k+154] = b[k+12]; b[k+12] = b[k+210]; b[k+210] = b[k+352]; b[k+352] = tmp
            tmp = b[k+173]; b[k+173] = b[k+11]; b[k+11] = b[k+191]; b[k+191] = b[k+353]; b[k+353] = tmp
            tmp = b[k+192]; b[k+192] = b[k+10]; b[k+10] = b[k+172]; b[k+172] = b[k+354]; b[k+354] = tmp
            tmp = b[k+211]; b[k+211] = b[k+9]; b[k+9] = b[k+153]; b[k+153] = b[k+355]; b[k+355] = tmp
            tmp = b[k+230]; b[k+230] = b[k+8]; b[k+8] = b[k+134]; b[k+134] = b[k+356]; b[k+356] = tmp
            tmp = b[k+249]; b[k+249] = b[k+7]; b[k+7] = b[k+115]; b[k+115] = b[k+357]; b[k+357] = tmp
            tmp = b[k+268]; b[k+268] = b[k+6]; b[k+6] = b[k+96]; b[k+96] = b[k+358]; b[k+358] = tmp
            tmp = b[k+287]; b[k+287] = b[k+5]; b[k+5] = b[k+77]; b[k+77] = b[k+359]; b[k+359] = tmp
            tmp = b[k+306]; b[k+306] = b[k+4]; b[k+4] = b[k+58]; b[k+58] = b[k+360]; b[k+360] = tmp
            tmp = b[k+325]; b[k+325] = b[k+3]; b[k+3] = b[k+39]; b[k+39] = b[k+361]; b[k+361] = tmp
            tmp = b[k+22]; b[k+22] = b[k+38]; b[k+38] = b[k+342]; b[k+342] = b[k+326]; b[k+326] = tmp
            tmp = b[k+41]; b[k+41] = b[k+37]; b[k+37] = b[k+323]; b[k+323] = b[k+327]; b[k+327] = tmp
            tmp = b[k+60]; b[k+60] = b[k+36]; b[k+36] = b[k+304]; b[k+304] = b[k+328]; b[k+328] = tmp
            tmp = b[k+79]; b[k+79] = b[k+35]; b[k+35] = b[k+285]; b[k+285] = b[k+329]; b[k+329] = tmp
            tmp = b[k+98]; b[k+98] = b[k+34]; b[k+34] = b[k+266]; b[k+266] = b[k+330]; b[k+330] = tmp
            tmp = b[k+117]; b[k+117] = b[k+33]; b[k+33] = b[k+247]; b[k+247] = b[k+331]; b[k+331] = tmp
            tmp = b[k+136]; b[k+136] = b[k+32]; b[k+32] = b[k+228]; b[k+228] = b[k+332]; b[k+332] = tmp
            tmp = b[k+155]; b[k+155] = b[k+31]; b[k+31] = b[k+209]; b[k+209] = b[k+333]; b[k+333] = tmp
            tmp = b[k+174]; b[k+174] = b[k+30]; b[k+30] = b[k+190]; b[k+190] = b[k+334]; b[k+334] = tmp
            tmp = b[k+193]; b[k+193] = b[k+29]; b[k+29] = b[k+171]; b[k+171] = b[k+335]; b[k+335] = tmp
            tmp = b[k+212]; b[k+212] = b[k+28]; b[k+28] = b[k+152]; b[k+152] = b[k+336]; b[k+336] = tmp
            tmp = b[k+231]; b[k+231] = b[k+27]; b[k+27] = b[k+133]; b[k+133] = b[k+337]; b[k+337] = tmp
            tmp = b[k+250]; b[k+250] = b[k+26]; b[k+26] = b[k+114]; b[k+114] = b[k+338]; b[k+338] = tmp
            tmp = b[k+269]; b[k+269] = b[k+25]; b[k+25] = b[k+95]; b[k+95] = b[k+339]; b[k+339] = tmp
            tmp = b[k+288]; b[k+288] = b[k+24]; b[k+24] = b[k+76]; b[k+76] = b[k+340]; b[k+340] = tmp
            tmp = b[k+307]; b[k+307] = b[k+23]; b[k+23] = b[k+57]; b[k+57] = b[k+341]; b[k+341] = tmp
            tmp = b[k+42]; b[k+42] = b[k+56]; b[k+56] = b[k+322]; b[k+322] = b[k+308]; b[k+308] = tmp
            tmp = b[k+61]; b[k+61] = b[k+55]; b[k+55] = b[k+303]; b[k+303] = b[k+309]; b[k+309] = tmp
            tmp = b[k+80]; b[k+80] = b[k+54]; b[k+54] = b[k+284]; b[k+284] = b[k+310]; b[k+310] = tmp
            tmp = b[k+99]; b[k+99] = b[k+53]; b[k+53] = b[k+265]; b[k+265] = b[k+311]; b[k+311] = tmp
            tmp = b[k+118]; b[k+118] = b[k+52]; b[k+52] = b[k+246]; b[k+246] = b[k+312]; b[k+312] = tmp
            tmp = b[k+137]; b[k+137] = b[k+51]; b[k+51] = b[k+227]; b[k+227] = b[k+313]; b[k+313] = tmp
            tmp = b[k+156]; b[k+156] = b[k+50]; b[k+50] = b[k+208]; b[k+208] = b[k+314]; b[k+314] = tmp
            tmp = b[k+175]; b[k+175] = b[k+49]; b[k+49] = b[k+189]; b[k+189] = b[k+315]; b[k+315] = tmp
            tmp = b[k+194]; b[k+194] = b[k+48]; b[k+48] = b[k+170]; b[k+170] = b[k+316]; b[k+316] = tmp
            tmp = b[k+213]; b[k+213] = b[k+47]; b[k+47] = b[k+151]; b[k+151] = b[k+317]; b[k+317] = tmp
            tmp = b[k+232]; b[k+232] = b[k+46]; b[k+46] = b[k+132]; b[k+132] = b[k+318]; b[k+318] = tmp
            tmp = b[k+251]; b[k+251] = b[k+45]; b[k+45] = b[k+113]; b[k+113] = b[k+319]; b[k+319] = tmp
            tmp = b[k+270]; b[k+270] = b[k+44]; b[k+44] = b[k+94]; b[k+94] = b[k+320]; b[k+320] = tmp
            tmp = b[k+289]; b[k+289] = b[k+43]; b[k+43] = b[k+75]; b[k+75] = b[k+321]; b[k+321] = tmp
            tmp = b[k+62]; b[k+62] = b[k+74]; b[k+74] = b[k+302]; b[k+302] = b[k+290]; b[k+290] = tmp
            tmp = b[k+81]; b[k+81] = b[k+73]; b[k+73] = b[k+283]; b[k+283] = b[k+291]; b[k+291] = tmp
            tmp = b[k+100]; b[k+100] = b[k+72]; b[k+72] = b[k+264]; b[k+264] = b[k+292]; b[k+292] = tmp
            tmp = b[k+119]; b[k+119] = b[k+71]; b[k+71] = b[k+245]; b[k+245] = b[k+293]; b[k+293] = tmp
            tmp = b[k+138]; b[k+138] = b[k+70]; b[k+70] = b[k+226]; b[k+226] = b[k+294]; b[k+294] = tmp
            tmp = b[k+157]; b[k+157] = b[k+69]; b[k+69] = b[k+207]; b[k+207] = b[k+295]; b[k+295] = tmp
            tmp = b[k+176]; b[k+176] = b[k+68]; b[k+68] = b[k+188]; b[k+188] = b[k+296]; b[k+296] = tmp
            tmp = b[k+195]; b[k+195] = b[k+67]; b[k+67] = b[k+169]; b[k+169] = b[k+297]; b[k+297] = tmp
            tmp = b[k+214]; b[k+214] = b[k+66]; b[k+66] = b[k+150]; b[k+150] = b[k+298]; b[k+298] = tmp
            tmp = b[k+233]; b[k+233] = b[k+65]; b[k+65] = b[k+131]; b[k+131] = b[k+299]; b[k+299] = tmp
            tmp = b[k+252]; b[k+252] = b[k+64]; b[k+64] = b[k+112]; b[k+112] = b[k+300]; b[k+300] = tmp
            tmp = b[k+271]; b[k+271] = b[k+63]; b[k+63] = b[k+93]; b[k+93] = b[k+301]; b[k+301] = tmp
            tmp = b[k+82]; b[k+82] = b[k+92]; b[k+92] = b[k+282]; b[k+282] = b[k+272]; b[k+272] = tmp
            tmp = b[k+101]; b[k+101] = b[k+91]; b[k+91] = b[k+263]; b[k+263] = b[k+273]; b[k+273] = tmp
            tmp = b[k+120]; b[k+120] = b[k+90]; b[k+90] = b[k+244]; b[k+244] = b[k+274]; b[k+274] = tmp
            tmp = b[k+139]; b[k+139] = b[k+89]; b[k+89] = b[k+225]; b[k+225] = b[k+275]; b[k+275] = tmp
            tmp = b[k+158]; b[k+158] = b[k+88]; b[k+88] = b[k+206]; b[k+206] = b[k+276]; b[k+276] = tmp
            tmp = b[k+177]; b[k+177] = b[k+87]; b[k+87] = b[k+187]; b[k+187] = b[k+277]; b[k+277] = tmp
            tmp = b[k+196]; b[k+196] = b[k+86]; b[k+86] = b[k+168]; b[k+168] = b[k+278]; b[k+278] = tmp
            tmp = b[k+215]; b[k+215] = b[k+85]; b[k+85] = b[k+149]; b[k+149] = b[k+279]; b[k+279] = tmp
            tmp = b[k+234]; b[k+234] = b[k+84]; b[k+84] = b[k+130]; b[k+130] = b[k+280]; b[k+280] = tmp
            tmp = b[k+253]; b[k+253] = b[k+83]; b[k+83] = b[k+111]; b[k+111] = b[k+281]; b[k+281] = tmp
            tmp = b[k+102]; b[k+102] = b[k+110]; b[k+110] = b[k+262]; b[k+262] = b[k+254]; b[k+254] = tmp
            tmp = b[k+121]; b[k+121] = b[k+109]; b[k+109] = b[k+243]; b[k+243] = b[k+255]; b[k+255] = tmp
            tmp = b[k+140]; b[k+140] = b[k+108]; b[k+108] = b[k+224]; b[k+224] = b[k+256]; b[k+256] = tmp
            tmp = b[k+159]; b[k+159] = b[k+107]; b[k+107] = b[k+205]; b[k+205] = b[k+257]; b[k+257] = tmp
            tmp = b[k+178]; b[k+178] = b[k+106]; b[k+106] = b[k+186]; b[k+186] = b[k+258]; b[k+258] = tmp
            tmp = b[k+197]; b[k+197] = b[k+105]; b[k+105] = b[k+167]; b[k+167] = b[k+259]; b[k+259] = tmp
            tmp = b[k+216]; b[k+216] = b[k+104]; b[k+104] = b[k+148]; b[k+148] = b[k+260]; b[k+260] = tmp
            tmp = b[k+235]; b[k+235] = b[k+103]; b[k+103] = b[k+129]; b[k+129] = b[k+261]; b[k+261] = tmp
            tmp = b[k+122]; b[k+122] = b[k+128]; b[k+128] = b[k+242]; b[k+242] = b[k+236]; b[k+236] = tmp
            tmp = b[k+141]; b[k+141] = b[k+127]; b[k+127] = b[k+223]; b[k+223] = b[k+237]; b[k+237] = tmp
            tmp = b[k+160]; b[k+160] = b[k+126]; b[k+126] = b[k+204]; b[k+204] = b[k+238]; b[k+238] = tmp
            tmp = b[k+179]; b[k+179] = b[k+125]; b[k+125] = b[k+185]; b[k+185] = b[k+239]; b[k+239] = tmp
            tmp = b[k+198]; b[k+198] = b[k+124]; b[k+124] = b[k+166]; b[k+166] = b[k+240]; b[k+240] = tmp
            tmp = b[k+217]; b[k+217] = b[k+123]; b[k+123] = b[k+147]; b[k+147] = b[k+241]; b[k+241] = tmp
            tmp = b[k+142]; b[k+142] = b[k+146]; b[k+146] = b[k+222]; b[k+222] = b[k+218]; b[k+218] = tmp
            tmp = b[k+161]; b[k+161] = b[k+145]; b[k+145] = b[k+203]; b[k+203] = b[k+219]; b[k+219] = tmp
            tmp = b[k+180]; b[k+180] = b[k+144]; b[k+144] = b[k+184]; b[k+184] = b[k+220]; b[k+220] = tmp
            tmp = b[k+199]; b[k+199] = b[k+143]; b[k+143] = b[k+165]; b[k+165] = b[k+221]; b[k+221] = tmp
            tmp = b[k+162]; b[k+162] = b[k+164]; b[k+164] = b[k+202]; b[k+202] = b[k+200]; b[k+200] = tmp
            tmp = b[k+181]; b[k+181] = b[k+163]; b[k+163] = b[k+183]; b[k+183] = b[k+201]; b[k+201] = tmp
