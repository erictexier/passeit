mkdir -p dev/${LOGNAME}/dsk_configuration/envi
mkdir -p dev/${LOGNAME}/packages

mkdir -p dev/dsk_configuration/envi/configs_and_packs/packs
mkdir -p dev/dsk_configuration/envi/configs_and_packs/configs
mkdir -p packages
dir=`pwd`
echo "add_pack('dskenvi')" > dev/dsk_configuration/envi/configs_and_packs/configs/init.py


TargetEnvi=dev/dsk_configuration/envi/configs_and_packs/packs/dskenvi.py
echo "import os" > ${TargetEnvi}
echo "base_release = '"${dir}"/packages/dskenvi'" >> ${TargetEnvi}
echo "version = ''" >> ${TargetEnvi}
echo "add_path('PYTHONPATH', os.path.join(base_release, version, 'python'))" >> ${TargetEnvi}
