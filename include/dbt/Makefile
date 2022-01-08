.DEFAULT_GOAL:=help

# Define which dbt version shall be installed, setup and compiled to get the target artifacts
DBT_VERSION = 0.19.2 0.20.0 0.21.0
NEW_DBT_VERSION = 1.0.0


.PHONY: initrapid-onboarding-exemplar
initrapid-onboarding-exemplar:  ## Init a clean dbt project from dbt labs rapid-onboarding-exemplar example
	rm -rf basesetup/rapid-onboarding-exemplar
	mkdir -p basesetup
	cd basesetup; git clone https://github.com/dbt-labs/rapid-onboarding-exemplar ; ls ; rm -rf rapid-onboarding-exemplar/.git
	cp -f basesetup/replace/agg_ship_modes_dynamic_pivot.sql basesetup/rapid-onboarding-exemplar/models/marts/aggregates/agg_ship_modes_dynamic_pivot.sql
	cp -f basesetup/replace/agg_ship_modes_hardcoded_pivot.sql basesetup/rapid-onboarding-exemplar/models/marts/aggregates/agg_ship_modes_hardcoded_pivot.sql


.PHONY: setup-dbt-profile
setup-dbt-profile:  ## Init a clean dbt project from dbt labs rapid-onboarding-exemplar example
	rm -rf $${HOME}/.dbt
	mkdir -p $${HOME}/.dbt
	cp basesetup/profiles/profiles.yml $${HOME}/.dbt/profiles.yml


.PHONY: uninstall-dbt
uninstall-dbt:  ## Uninstall all dbt packages
	for dbtversion in $(DBT_VERSION)  ; do \
		pip uninstall dbt==$$dbtversion -y ; \
		pip uninstall dbt-bigquery -y ; \
		pip uninstall dbt-core -y ; \
		pip uninstall dbt-extractor  -y ; \
		pip uninstall dbt-postgres -y ; \
		pip uninstall dbt-redshift -y ; \
		pip uninstall dbt-snowflake -y ; \
	done



.PHONY: init
init:  initrapid-onboarding-exemplar setup-dbt-profile ## Init a new dbt project with postgres connection, install dbt and run dbt debug
	for dbtversion in $(DBT_VERSION)  ; do \
	    rm -rf rapid-onboarding-exemplar_$$dbtversion ; \
		mkdir rapid-onboarding-exemplar_$$dbtversion ; \
		cp -a basesetup/rapid-onboarding-exemplar/. rapid-onboarding-exemplar_$$dbtversion ; \
		pip uninstall dbt==$$dbtversion -y ; \
		pip install dbt==$$dbtversion ; \
		cd rapid-onboarding-exemplar_$$dbtversion ; dbt deps ; dbt compile --no-version-check ; \
		pip uninstall dbt==$$dbtversion -y ; \
		pip uninstall dbt-bigquery -y ; \
		pip uninstall dbt-core -y ; \
		pip uninstall dbt-extractor  -y ; \
		pip uninstall dbt-postgres -y ; \
		pip uninstall dbt-redshift -y ; \
		pip uninstall dbt-snowflake  -y ; \
		cd .. ; \
	done
	for dbtversion in $(NEW_DBT_VERSION)  ; do \
	    rm -rf rapid-onboarding-exemplar_$$dbtversion ; \
		mkdir rapid-onboarding-exemplar_$$dbtversion ; \
		cp -a basesetup/rapid-onboarding-exemplar/. rapid-onboarding-exemplar_$$dbtversion ; \
		pip uninstall pip install dbt-postgres==$$dbtversion -y ; \
		pip install dbt-postgres==$$dbtversion ; \
		cd rapid-onboarding-exemplar_$$dbtversion ; dbt deps ; dbt compile --no-version-check ; \
		pip uninstall dbt==$$dbtversion -y ; \
		pip uninstall dbt-bigquery -y ; \
		pip uninstall dbt-core -y ; \
		pip uninstall dbt-extractor  -y ; \
		pip uninstall dbt-postgres -y ; \
		pip uninstall dbt-redshift -y ; \
		pip uninstall dbt-snowflake  -y ; \
		cd .. ; \
	done


.PHONY: copy-manifest-test-directory
copy-manifest-test-directory:  ## Copy all generated dbt manifest an cp in in target repo
	for dbtversion in $(DBT_VERSION)  ; do \
	    cp rapid-onboarding-exemplar_$$dbtversion/target/manifest.json ../../tests/data/manifest_$$dbtversion.json ; \
	done

.PHONY: installdbt
installdbt:  ## Init a clean dbt project from dbt labs rapid-onboarding-exemplar example
	pip install dbt==0.20.0


.PHONY: help
help: ## Show this help message.
	@echo
	@echo 'targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	@echo
	@echo 'options:'

