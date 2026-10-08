#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

blob_fixups: blob_fixups_user_type = {
    'system/priv-app/MiuiCamera/MiuiCamera.apk': blob_fixup()
        .apktool_patch('patches'),
    'system/lib64/libmicampostproc_client.so': blob_fixup()
        .remove_needed('libhidltransport.so'),
    'system/lib64/libcamera_algoup_jni.xiaomi.so': blob_fixup()
        .add_needed('libgui_camera_shim.so')
        .add_needed('libcamera_metadata_shim_apollo.so')
        # Android 16: Surface::connect(int) is at vtable offset 0xc8.
        .sig_replace('08 A9 40 F9', '08 65 40 F9')
        .sig_replace('F4 03 00 F9 54 01 00 B4', 'FF 03 00 F9 0A 00 00 14'),
    'system/lib64/libcamera_mianode_jni.xiaomi.so': blob_fixup()
        .add_needed('libgui_shim_miuicamera.so')
        .add_needed('libcamera_metadata_shim_apollo.so'),
    'vendor/lib64/libarcsoft_single_chart_calibration.so': blob_fixup()
        .replace_needed('libstdc++.so', 'libstdc++_vendor.so'),
}  # fmt: skip

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'libgrallocutils',
    ): lib_fixup_remove,
}

namespace_imports = [
    'hardware/qcom-caf/common/libqti-perfd-client',
    'vendor/qcom/opensource/display',
    'vendor/xiaomi/apollo',
]

module = ExtractUtilsModule(
    'camera',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
