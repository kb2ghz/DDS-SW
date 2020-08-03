# TTL logic based Direct Digital Synthesis (DDS) Project
# Mike McCann KB2GHZ

ASM = gpasm
OPT = -i --hex-format inhx8m --dos -w1

DDS : DDS.ASM
	$(ASM) $(OPT) $@.ASM 

