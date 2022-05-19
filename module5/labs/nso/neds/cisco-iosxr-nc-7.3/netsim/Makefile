include $(NCS_DIR)/src/ncs/build/include.netsim.mk

## If you need additional init xml files, put them in
## the current directory, and they will be picked up here.

YDIR = ../src/yang
TDIR = ../src/tmp-yang
XML  = $(wildcard *.xml)
XML  += $(NCS_DIR)/netsim/confd/var/confd/cdb/aaa_init.xml

EXTRA_FILES  = confd.conf.netsim
SKIP_MODULES = tailf-aaa.yang

YANG         = $(notdir $(wildcard $(YDIR)/*.yang))
SUBMODULES   = $(notdir $(shell grep -l belongs-to $(YDIR)/*.yang | xargs grep -l submodule))
YANG_MODULES = $(filter-out $(SUBMODULES) $(SKIP_MODULES),$(YANG))

FXS = $(YANG_MODULES:%.yang=%.fxs)

FLAGS = -w TAILF_MUST_NEED_DEPENDENCY --yangpath $(TDIR) --prefix module-name

all:
	$(MAKE) $(FXS)

%.fxs:  $(TDIR)/%.yang
	$(CONFDC) $(FLAGS) -c -o $@ $<

# Invoked by netsim, who will sed substitute the %var% PORT variables
# in the confd.conf.netsim file
# The install target here will be invoked multiple times by ncs-netsim,
# once for each device in the simulation network
# The following env variable will be set when ncs-netsim invokes this
# install target
# - DEST_DIR this is where all the files shall go, it's the directory
#   that will be used as execution environment for this ConfD instance
# - NAME this is the name of the managed device
# - COUNTER this is the number of the managed device

install:
	@if [ -z "$${DEST_DIR}" ]; then echo "No DEST_DIR  var"; exit 1; fi
	@if [ ! -d "$${DEST_DIR}" ]; then "echo No DEST_DIR"; exit 1; fi
	mkdir $${DEST_DIR}/cdb 2>/dev/null || true
	mkdir $${DEST_DIR}/logs 2>/dev/null || true
	for i in $(XML); do \
		sed -e 's/%NAME%/$(NAME)/g' -e 's/%COUNTER%/$(COUNTER)/g' -e 's/%TWO_DIGIT_COUNTER%/$(TWO_DIGIT_COUNTER)/g' \
		  $$i > $${DEST_DIR}/cdb/`basename $$i`; \
	done
	cp -f $(FXS) $${DEST_DIR}
	cp -f $(EXTRA_FILES) $${DEST_DIR} || true
	cp -af $(NCS_DIR)/netsim/confd/etc/confd/ssh $${DEST_DIR}
clean:
	@rm -f *.fxs
