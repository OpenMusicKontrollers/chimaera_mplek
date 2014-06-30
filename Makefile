TARGETS := mplek_12.0mm.stl
TARGETS += mplek_12.5mm.stl
TARGETS += mplek_13.0mm.stl 
TARGETS += mplek_13.5mm.stl 
TARGETS += mplek_14.0mm.stl 
TARGETS += mplek_14.5mm.stl 
TARGETS += mplek_15.0mm.stl 
TARGETS += mplek_15.5mm.stl 
TARGETS += mplek_16.0mm.stl 
TARGETS += mplek_16.5mm.stl 
TARGETS += mplek_17.0mm.stl 
TARGETS += mplek_17.5mm.stl 
TARGETS += mplek_18.0mm.stl 
TARGETS += mplek_18.5mm.stl 
TARGETS += mplek_19.0mm.stl 
TARGETS += mplek_19.5mm.stl 
TARGETS += mplek_20.0mm.stl 
TARGETS += mplek_20.5mm.stl
TARGETS += mplek_21.0mm.stl
TARGETS += mplek_21.5mm.stl
TARGETS += mplek_22.0mm.stl
TARGETS += mplek_22.5mm.stl
TARGETS += mplek_23.0mm.stl
TARGETS += mplek_23.5mm.stl
TARGETS += mplek_24.0mm.stl
TARGETS += mplek_24.5mm.stl
TARGETS += mplek_25.0mm.stl
TARGETS += mplek_25.5mm.stl
TARGETS += mplek_26.0mm.stl
TARGETS += mplek_26.5mm.stl

TARGETS += mstamp.stl

all: $(TARGETS)

mplek_%mm.stl: mplek.py
	blender -P $< -- $* $@

mstamp.stl: mstamp.py
	blender -P $< -- $@

clean:
	rm -f $(TARGETS)
