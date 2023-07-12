---
title: UPlayerCapturePointComponent
type: class
aliases: UPlayerCapturePointComponent
share: false

---

# UPlayerCapturePointComponent





Inherits from UActorComponent, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[ActivatePlayerCapturePoint]]**() |
| void | **[[BeginOverlap]]**(AActor * OverlappedActor, AActor * OtherActor) |
| void | **[[DeactivatePlayerCapturePoint]]**() |
| void | **[[EndOverlap]]**(AActor * OverlappedActor, AActor * OtherActor) |
| bool | **[[GetIsBlocked]]**() |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| TArray< [FPlayerCaptureData](/docs/SDK/Source/Classes/structFPlayerCaptureData.md) > | **[[GetPlayersCaptureData]]**() |
| void | **[[OnRep_IsBlocked]]**() |
| void | **[[OnRep_PlayersInPlayerCapturePoint]]**() |
| void | **[[OnRep_Properties]]**() |
| void | **[[OnTrackedCharacterDestroyed]]**(AActor * DestroyedActor) |
| void | **[[OnTrackedCharacterKilled]]**(const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & DamageEvent) |
| bool | **[[PlayerSatisfiesCaptureRequirments]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Player) |
| void | **[[RefreshActorsInCaptureZone]]**() |
| void | **[[ResetCapturePoint]]**() |
| void | **[[SetPlayerCapturePointProperties]]**([FPlayerCapturePointComponentProperties](/docs/SDK/Source/Classes/structFPlayerCapturePointComponentProperties.md) Props) |
| | **[[UPlayerCapturePointComponent]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| FBlockedStatusUpdated | **[[OnBlockedStatusUpdated]]**  |
| FPlayerCompletedCapture | **[[OnPlayerCompletedCapture]]**  |
| [FPlayerCapturePointComponentProperties](/docs/SDK/Source/Classes/structFPlayerCapturePointComponentProperties.md) | **[[PlayerCapturePointComponentProperties]]**  |
| [FReplicatedArray_PlayerCaptureData](/docs/SDK/Source/Classes/structFReplicatedArray__PlayerCaptureData.md) | **[[PlayersCapturingData]]**  |
| FPlayersUpdated | **[[PlayersInCaptureVolumeChanged]]**  |
| [FReplicatedArray_ATBLCharacterPtr](/docs/SDK/Source/Classes/structFReplicatedArray__ATBLCharacterPtr.md) | **[[PlayersInVolume]]**  |
| [FReplicated_FPlayerCapturePointComponentProperties](/docs/SDK/Source/Classes/structFReplicated__FPlayerCapturePointComponentProperties.md) | **[[ReplicatedTeamCapturePointComponentProperties]]**  |
| [FReplicated_Bool](/docs/SDK/Source/Classes/structFReplicated__Bool.md) | **[[bIsBlocked]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200