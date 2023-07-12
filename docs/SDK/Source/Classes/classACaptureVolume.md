---
title: ACaptureVolume
type: class
aliases: ACaptureVolume
share: false

---

# ACaptureVolume





Inherits from [ATBLActor](/docs/SDK/Source/Classes/classATBLActor.md), AActor, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

Inherited by [ALoadoutVolume](/docs/SDK/Source/Classes/classALoadoutVolume.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[ACaptureVolume]]**() |
| void | **[[AddPlayerToCapturePoint]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Player) |
| void | **[[BeginOverlap]]**(AActor * OverlappedActor, AActor * OtherActor) |
| void | **[[ClientBeginOverlap]]**(AActor * OverlappedActor, AActor * OtherActor) |
| void | **[[ClientEndOverlap]]**(AActor * OverlappedActor, AActor * OtherActor) |
| void | **[[EndOverlap]]**(AActor * OverlappedActor, AActor * OtherActor) |
| [ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * | **[[GetControllingTeam]]**(bool & IsTie) |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| void | **[[OnCaptureStateCaptured]]**() |
| void | **[[OnCaptureStateCapturing]]**() |
| void | **[[OnCaptureStateContested]]**() |
| void | **[[OnCaptureStateIdle]]**() |
| void | **[[OnCaptureStateNeutralizing]]**() |
| void | **[[OnRep_CaptureState]]**() |
| void | **[[OnTrackedCharacterDestroyed]]**(AActor * DestroyedActor) |
| void | **[[OnTrackedCharacterKilled]]**(const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & DamageEvent) |
| bool | **[[PlayerSatisfiesCaptureRequirments]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Player) |
| void | **[[RefreshActorsInCaptureZone]]**() |
| void | **[[RemovePlayerFromCapturePoint]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Player) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| UBoxComponent * | **[[CaptureBox]]**  |
| UCapsuleComponent * | **[[CaptureCapsule]]**  |
| TEnumAsByte< ECaptureVolumeControlType::Type > | **[[CapturePointRule]]**  |
| TEnumAsByte< ECapturePointState::Type > | **[[CurrentCaptureState]]**  |
| TArray< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * > | **[[PlayersInCaptureVolume]]**  |
| FUpdatePlayersInCapturePoint | **[[PlayersInCaptureVolumeChanged]]**  |
| TEnumAsByte< ECapturePointState::Type > | **[[PreviousCaptureState]]**  |
| bool | **[[bUseCaptureBoxComponent]]**  |
| bool | **[[bUseCaptureCapsuleComponent]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200