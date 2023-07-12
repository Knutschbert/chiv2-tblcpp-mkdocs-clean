---
title: UTeamCapturePointComponent
type: class
aliases: UTeamCapturePointComponent
share: false

---

# UTeamCapturePointComponent





Inherits from UActorComponent, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md), [ITBLBlueprintCompilerInterface](/docs/SDK/Source/Classes/classITBLBlueprintCompilerInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[ActivateTeamCapturePoint]]**() |
| void | **[[BeginOverlap]]**(AActor * OverlappedActor, AActor * OtherActor) |
| void | **[[DeactivateTeamCapturePoint]]**() |
| void | **[[EndOverlap]]**(AActor * OverlappedActor, AActor * OtherActor) |
| [ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * | **[[GetControllingTeam]]**(bool & IsTie) |
| bool | **[[GetIsImmune]]**() |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| [ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * | **[[GetOwningTeam]]**() |
| int32 | **[[GetPlayerNumbersForFaction]]**(EFaction Faction) |
| [ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * | **[[GetProgressGainedByTeam]]**() |
| void | **[[OnActivated]]**(UActorComponent * Component, bool bReset) |
| void | **[[OnDeactivated]]**(UActorComponent * Component) |
| void | **[[OnRep_CaptureState]]**() |
| void | **[[OnRep_ControllingTeamChanged]]**() |
| void | **[[OnRep_PlayersInTeamCapturePoint]]**() |
| void | **[[OnRep_Properties]]**() |
| void | **[[OnTrackedCharacterDestroyed]]**(AActor * DestroyedActor) |
| void | **[[OnTrackedCharacterKilled]]**(const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & DamageEvent) |
| bool | **[[PlayerSatisfiesCaptureRequirments]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Player) |
| void | **[[RefreshActorsInCaptureZone]]**() |
| void | **[[ResetCapturePoint]]**() |
| void | **[[SetCaptureState]]**(TEnumAsByte< ETeamCapturePointComponentState::Type > NewState) |
| void | **[[SetIsDefendingTeamAllowedToGainScore]]**(bool Enabled) |
| void | **[[SetTeamCapturePointProperties]]**([FTeamCapturePointComponentProperties](/docs/SDK/Source/Classes/structFTeamCapturePointComponentProperties.md) Props) |
| | **[[UTeamCapturePointComponent]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[OnRep_OwningTeamChanged]]**() |
| void | **[[OnRep_Progress]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| FCPStateChanged | **[[CaptureStateChanged]]**  |
| [FReplicated_ATBLTeamPtr](/docs/SDK/Source/Classes/structFReplicated__ATBLTeamPtr.md) | **[[ControllingTeam]]**  |
| [FReplicated_ECapturePointState](/docs/SDK/Source/Classes/structFReplicated__ECapturePointState.md) | **[[CurrentCaptureState]]**  |
| [FDisplayComponentControls](/docs/SDK/Source/Classes/structFDisplayComponentControls.md) | **[[DisplayComponentControls]]**  |
| [FObjectiveStatusDisplayComponentStruct](/docs/SDK/Source/Classes/structFObjectiveStatusDisplayComponentStruct.md) | **[[ObjectiveStatusDisplay]]**  |
| FCPOwningTeamHasChanged | **[[OnControllingTeamHasChanged]]**  |
| FCPOwningTeamHasChanged | **[[OnOwningTeamHasChanged]]**  |
| FCPPlayerAdded | **[[OnPlayerAdded]]**  |
| FCPPlayerAdded | **[[OnPlayerRemoved]]**  |
| FCPProgressChange | **[[OnProgressChanged]]**  |
| [FReplicated_ATBLTeamPtr](/docs/SDK/Source/Classes/structFReplicated__ATBLTeamPtr.md) | **[[OwningTeam]]**  |
| [FReplicatedArray_ATBLCharacterPtr](/docs/SDK/Source/Classes/structFReplicatedArray__ATBLCharacterPtr.md) | **[[PlayersInCaptureVolume]]**  |
| FPlayersUpdateInTeamCPComponent | **[[PlayersInCaptureVolumeChanged]]**  |
| [FReplicated_ECapturePointState](/docs/SDK/Source/Classes/structFReplicated__ECapturePointState.md) | **[[PreviousCaptureState]]**  |
| [FReplicated_Float](/docs/SDK/Source/Classes/structFReplicated__Float.md) | **[[Progress]]**  |
| [FReplicated_ATBLTeamPtr](/docs/SDK/Source/Classes/structFReplicated__ATBLTeamPtr.md) | **[[ProgressGainedByTeam]]**  |
| [FReplicated_FTeamCapturePointComponentProperties](/docs/SDK/Source/Classes/structFReplicated__FTeamCapturePointComponentProperties.md) | **[[ReplicatedTeamCapturePointComponentProperties]]**  |
| [FTeamCapturePointComponentProperties](/docs/SDK/Source/Classes/structFTeamCapturePointComponentProperties.md) | **[[TeamCapturePointComponentProperties]]**  |
| FCPTickEvent | **[[TickEventFire]]**  |
| [FReplicated_Bool](/docs/SDK/Source/Classes/structFReplicated__Bool.md) | **[[bIsImmune]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [FDataTableRowSelection](/docs/SDK/Source/Classes/structFDataTableRowSelection.md) | **[[CaptureIntervalScoreEvent]]**  |
| float | **[[CaptureIntervalScoreInterval]]**  |
| TMap< uint32, TWeakObjectPtr< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > > | **[[CharacterIDMap]]**  |
| TArray< AActor * > | **[[OtherOverlapActors]]**  |
| TArray< UPrimitiveComponent * > | **[[OverlapComponents]]**  |
| TMap< AActor *, [FOverlappedCharacterList](/docs/SDK/Source/Classes/structFOverlappedCharacterList.md) > | **[[TrackedCharactersByActor]]**  |
| bool | **[[bAwardCaptureInterval]]**  |
| bool | **[[bAwardScoreWhenCaptured]]**  |
| bool | **[[bDefenderCanGetScore]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:01 +0200