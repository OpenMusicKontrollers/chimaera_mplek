TARGETS := mplek_12.0mm.dae
TARGETS += mplek_12.5mm.dae
TARGETS += mplek_13.0mm.dae
TARGETS += mplek_13.5mm.dae
TARGETS += mplek_14.0mm.dae
TARGETS += mplek_14.5mm.dae
TARGETS += mplek_15.0mm.dae
TARGETS += mplek_15.5mm.dae
TARGETS += mplek_16.0mm.dae
TARGETS += mplek_16.5mm.dae
TARGETS += mplek_17.0mm.dae
TARGETS += mplek_17.5mm.dae
TARGETS += mplek_18.0mm.dae
TARGETS += mplek_18.5mm.dae
TARGETS += mplek_19.0mm.dae
TARGETS += mplek_19.5mm.dae
TARGETS += mplek_20.0mm.dae
TARGETS += mplek_20.5mm.dae
TARGETS += mplek_21.0mm.dae
TARGETS += mplek_21.5mm.dae
TARGETS += mplek_22.0mm.dae
TARGETS += mplek_22.5mm.dae
TARGETS += mplek_23.0mm.dae
TARGETS += mplek_23.5mm.dae
TARGETS += mplek_24.0mm.dae
TARGETS += mplek_24.5mm.dae
TARGETS += mplek_25.0mm.dae
TARGETS += mplek_25.5mm.dae
TARGETS += mplek_26.0mm.dae
TARGETS += mplek_26.5mm.dae

TARGETS += mstamp.dae

all: $(TARGETS)

mplek_%mm.dae: mplek.py
	blender -P $< -- $* $@

mstamp.dae: mstamp.py
	blender -P $< -- $@

clean:
	rm -f $(TARGETS)
