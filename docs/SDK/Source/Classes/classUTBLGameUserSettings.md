---
title: UTBLGameUserSettings
type: class
aliases: UTBLGameUserSettings
share: false

---

# UTBLGameUserSettings





Inherits from UGameUserSettings

## Public Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[[AreHintsEnabled]]**() |
| TEnumAsByte< EAllyMarkerLevel::Type > | **[[GetAllyMarkerLevel]]**() |
| int32 | **[[GetAmbientCorpseQuality]]**() const |
| float | **[[GetBloodDecalLifeTime]]**() const |
| bool | **[[GetEnableCrossPlayMatchmaking]]**() |
| TEnumAsByte< EGoreLevel::Type > | **[[GetGoreLevel]]**() |
| TEnumAsByte< EKillFeedFilter::Type > | **[[GetKillFeedFilter]]**() |
| float | **[[GetMasterVolume]]**() |
| int32 | **[[GetMotionBlurQuality]]**() const |
| [UTBLOptionsScreen](/docs/SDK/Source/Classes/classUTBLOptionsScreen.md) * | **[[GetOptionsScreen]]**() |
| uint8 | **[[GetPreferredFaction]]**() |
| int32 | **[[GetServerBrowserNumFreeSlotServers]]**() const |
| bool | **[[IsAmbientFXEnabled]]**() const |
| bool | **[[IsCombatNumbersEnabled]]**() |
| bool | **[[IsDX12Enabled]]**() |
| bool | **[[IsDamageMultipliersEnabled]]**() |
| bool | **[[IsDynamicCrosshairEnabled]]**() |
| bool | **[[IsGamepadYInverted]]**() const |
| bool | **[[IsHeadBobEnabled]]**() |
| bool | **[[IsLoadoutDisplayOnFirstDeathEnabled]]**() const |
| bool | **[[IsRagdollEnabled]]**() |
| bool | **[[IsServerBrowserHideEmptyServersEnabled]]**() const |
| bool | **[[IsServerBrowserHideFullServersEnabled]]**() const |
| bool | **[[IsServerBrowserHideHighPingEnabled]]**() const |
| void | **[[OnReadUserFileComplete]]**(const FPlatformInterfaceDelegateResult & Result) |
| void | **[[SaveCloudUserSettingsIfDirty]]**() |
| void | **[[SetDX12Enabled]]**(bool Value) |
| void | **[[SetPreferredFaction]]**(uint8 InPreferredFaction) |
| void | **[[SetServerBrowserHideEmptyServersEnabled]]**(bool bEnabled) |
| void | **[[SetServerBrowserHideFullServers]]**(bool bEnabled) |
| void | **[[SetServerBrowserHideHighPingEnabled]]**(bool bEnabled) |
| void | **[[SetServerBrowserNumFreeSlotServers]]**(int32 Num) |
| | **[[UTBLGameUserSettings]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| int32 | **[[AmbientCorpseQuality]]**  |
| int32 | **[[BloodDecalLifetime]]**  |
| EColorVisionDeficiency | **[[ColorVisionDeficiency]]**  |
| int32 | **[[ColorVisionDeficiencyCorrectionStrength]]**  |
| bool | **[[DFAO]]**  |
| bool | **[[EnableUpdateRateOptimizations]]**  |
| float | **[[GUIScale]]**  |
| TArray< UCurveFloat * > | **[[GamepadLookResponseCurves]]**  |
| float | **[[Gamma]]**  |
| EHapticsVolumeSettings | **[[HapticsVolumeSetting]]**  |
| int32 | **[[MaxFPS]]**  |
| float | **[[MotionBlurAmountDefault]]**  |
| float | **[[MotionBlurAmountMax]]**  |
| int32 | **[[MotionBlurQuality]]**  |
| float | **[[MouseFocusSensitivity]]**  |
| float | **[[MouseSensitivity]]**  |
| [UTBLOptionsScreen](/docs/SDK/Source/Classes/classUTBLOptionsScreen.md) * | **[[OptionsScreen]]**  |
| int32 | **[[PreferredDLSSOperatingMode]]**  |
| uint8 | **[[PreferredFaction]]**  |
| int32 | **[[PreferredXESSOperatingMode]]**  |
| int32 | **[[PreferrredIntelVRSSetting]]**  |
| EProConsoleOption | **[[ProConsoleSetting]]**  |
| float | **[[RagdollLifetime]]**  |
| float | **[[ResolutionScaleModifier]]**  |
| uint8 | **[[SmoothedFrameRateRange]]**  |
| uint32 | **[[TBLVersion]]**  |
| bool | **[[bAmbientFXEnabled]]**  |
| bool | **[[bConsoleEnabled]]**  |
| bool | **[[bDisableCrossPlayMatchmaking]]**  |
| bool | **[[bHeadphonesMode]]**  |
| bool | **[[bRagdollEnabled]]**  |
| bool | **[[bUseAdaptiveTriggers]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200