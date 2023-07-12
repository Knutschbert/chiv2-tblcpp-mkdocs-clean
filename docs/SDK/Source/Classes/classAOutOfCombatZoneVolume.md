---
title: AOutOfCombatZoneVolume
type: class
aliases: AOutOfCombatZoneVolume
share: false

---

# AOutOfCombatZoneVolume





Inherits from AActor

Inherited by [AOutOfCombatZoneVolume_Box](/docs/SDK/Source/Classes/classAOutOfCombatZoneVolume__Box.md), [AOutOfCombatZoneVolume_Ellipse](/docs/SDK/Source/Classes/classAOutOfCombatZoneVolume__Ellipse.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[AOutOfCombatZoneVolume]]**() |
| void | **[[ActivateDeactivate]]**(EOutOfCombatZoneVolumeActivateDeactivateAction Action) |
| bool | **[[CanResizeToNextThreshold]]**(float NewPlayerRatio, float NewTimeRatio) |
| void | **[[ClientSetVisualizationFade]]**([ATBLPlayerController](/docs/SDK/Source/Classes/classATBLPlayerController.md) * LocalController, bool bShouldFade) |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| [FCombatZoneVolumeSizeParam](/docs/SDK/Source/Classes/structFCombatZoneVolumeSizeParam.md) | **[[GetNextZoneThreshold]]**() |
| bool | **[[IsActive]]**() |
| bool | **[[IsInCombatZone]]**(const FVector & Point) const |
| void | **[[OnStateChanged]]**(EOutOfCombatZoneVolumeActivateDeactivateAction StateChanged) |
| void | **[[ResetCombatZoneThreshold]]**() |
| void | **[[ResizeCombatZoneBasedOnNextThreshold]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TSubclassOf< [AOutOfCombatZoneAuthority](/docs/SDK/Source/Classes/classAOutOfCombatZoneAuthority.md) > | **[[AuthorityClass]]**  |
| USceneComponent * | **[[DefaultSceneComponent]]**  |
| EFaction | **[[Faction]]**  |
| UStaticMeshComponent * | **[[PreviewMeshComponent]]**  |
| TArray< [FCombatZoneVolumeSizeParam](/docs/SDK/Source/Classes/structFCombatZoneVolumeSizeParam.md) > | **[[ZoneSizeThresholdArray]]**  |
| bool | **[[bShouldShrinkZoneAccordingToThresholds]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200