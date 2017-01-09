TARGETS := mplek_12.0mm
TARGETS += mplek_12.5mm
TARGETS += mplek_13.0mm
TARGETS += mplek_13.5mm
TARGETS += mplek_14.0mm
TARGETS += mplek_14.5mm
TARGETS += mplek_15.0mm
TARGETS += mplek_15.5mm
TARGETS += mplek_16.0mm
TARGETS += mplek_16.5mm
TARGETS += mplek_17.0mm
TARGETS += mplek_17.5mm
TARGETS += mplek_18.0mm
TARGETS += mplek_18.5mm
TARGETS += mplek_19.0mm
TARGETS += mplek_19.5mm
TARGETS += mplek_20.0mm
TARGETS += mplek_20.5mm
TARGETS += mplek_21.0mm
TARGETS += mplek_21.5mm
TARGETS += mplek_22.0mm
TARGETS += mplek_22.5mm
TARGETS += mplek_23.0mm
TARGETS += mplek_23.5mm
TARGETS += mplek_24.0mm
TARGETS += mplek_24.5mm
TARGETS += mplek_25.0mm
TARGETS += mplek_25.5mm
TARGETS += mplek_26.0mm
TARGETS += mplek_26.5mm

TARGETS += mstamp

TARGETS += mstamp2

TARGETS_DAE := $(TARGETS:=.dae)
TARGETS_STL := $(TARGETS:=.stl)

all: $(TARGETS_STL)

mplek_%mm.dae: mplek.py
	blender -P $< -- $* $@

mplek_%mm.stl: mplek.py
	blender -P $< -- $* $@

mstamp.dae: mstamp.py
	blender -P $< -- $@

mstamp.stl: mstamp.py
	blender -P $< -- $@

mstamp2.dae: mstamp2.py
	blender -P $< -- $@

mstamp2.stl: mstamp2.py
	blender -P $< -- $@

clean:
	rm -f $(TARGETS_DAE) $(TARGETS_STL)
