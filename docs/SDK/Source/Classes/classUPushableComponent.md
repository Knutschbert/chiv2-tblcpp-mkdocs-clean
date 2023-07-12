---
title: UPushableComponent
type: class
aliases: UPushableComponent
share: false

---

# UPushableComponent





Inherits from UActorComponent, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md), [ITBLBlueprintCompilerInterface](/docs/SDK/Source/Classes/classITBLBlueprintCompilerInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[ActivatePushable]]**(bool Active) |
| void | **[[AddPushableAuthorityProgress]]**(float Progress) |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| float | **[[GetProgressToNextPoint]]**() const |
| void | **[[GetPushableProgressSummary]]**(float & Progress, [FPushableEndPoint](/docs/SDK/Source/Classes/structFPushableEndPoint.md) & OutCurrentEndPoint, float & ProgressPercent) |
| UPrimitiveComponent * | **[[GetPushingCollisionComponent]]**() |
| TArray< UPrimitiveComponent * > | **[[GetSimulatingPhysicsComponents]]**() |
| bool | **[[IsFollower]]**() const |
| bool | **[[IsIndependent]]**() const |
| bool | **[[IsLeader]]**() const |
| bool | **[[IsPushableActive]]**() |
| void | **[[OnCaptureStateChanged]]**(TEnumAsByte< ETeamCapturePointComponentState::Type > CaptureState) |
| void | **[[OnControllingTeamHasChanged]]**([ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * ControllingTeam) |
| void | **[[OnHealthChanged]]**(float Amount, AActor * Initiator) |
| void | **[[OnOwningTeamHasChanged]]**([ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * OwningTeam) |
| void | **[[OnPlayersInCaptureVolumeChanged]]**(const TArray< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * > & Players) |
| void | **[[OnRep_CurrentEndPoint]]**() |
| void | **[[OnRep_FollowerPushableComponentProperties]]**() |
| void | **[[OnRep_FollowerPushables]]**() |
| void | **[[OnRep_PushableActive]]**() |
| void | **[[OnRep_PushableComponentProperties]]**() |
| void | **[[OnRep_PushableEndPoints]]**() |
| void | **[[OnRep_PushableMovementType]]**() |
| void | **[[OnRep_PushableProgressAuthority]]**() |
| void | **[[OnRep_ReplicatedMovementState]]**() |
| void | **[[OnRep_ReplicatedSplineActor]]**() |
| void | **[[ProceedToNextEndPoint]]**() |
| void | **[[ReConfigurePushable]]**(EPushableMovementType NewMovementType, [FPushableComponentProperties](/docs/SDK/Source/Classes/structFPushableComponentProperties.md) IndependentAndLeaderProperties, [FFollowerPushableComponentProperties](/docs/SDK/Source/Classes/structFFollowerPushableComponentProperties.md) FollowerProperties, [APushableSplineActor](/docs/SDK/Source/Classes/classAPushableSplineActor.md) * NewSplineActor, TArray< [FPushableEndPoint](/docs/SDK/Source/Classes/structFPushableEndPoint.md) > NewEndPoints, TArray< AActor * > NewFollowerPushables, float TimeToComplete, float TravelSpeedToNewSpline, FLatentActionInfo LatentInfo) |
| void | **[[ResetProgress]]**(float NewProgress) |
| void | **[[ReversePushableByDistance]]**(float Distance) |
| void | **[[SetCurrentEndPointCinematic]]**(bool CinematicEndPoint) |
| void | **[[SetFollowerPushableComponentProperties]]**([FFollowerPushableComponentProperties](/docs/SDK/Source/Classes/structFFollowerPushableComponentProperties.md) Props) |
| void | **[[SetPushableComponentProperties]]**([FPushableComponentProperties](/docs/SDK/Source/Classes/structFPushableComponentProperties.md) Props) |
| void | **[[SetPushableMovementType]]**(EPushableMovementType NewMovementType) |
| void | **[[SetPushingCollisionComponent]]**(UPrimitiveComponent * NewPushingCollisionComponent) |
| void | **[[SkipToEndOfCurrentEndPoint]]**() |
| | **[[UPushableComponent]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [FReplicated_Int32](/docs/SDK/Source/Classes/structFReplicated__Int32.md) | **[[CurrentEndPoint]]**  |
| float | **[[CurrentSpeedScale]]**  |
| [FFollowerPushableComponentProperties](/docs/SDK/Source/Classes/structFFollowerPushableComponentProperties.md) | **[[FollowerPushableComponentProperties]]**  |
| TArray< AActor * > | **[[FollowerPushables]]**  |
| float | **[[HitchTime]]**  |
| float | **[[LeaderStartingDistance]]**  |
| float | **[[MaxSpeed]]**  |
| [UHudMarkerDisplayComponent](/docs/SDK/Source/Classes/classUHudMarkerDisplayComponent.md) * | **[[ObjectiveStatusDisplay]]**  |
| FOnPushableActivated | **[[OnPushableActivated]]**  |
| FOnPushableCompleted | **[[OnPushableCompleted]]**  |
| FOnPushableMovementTypeChanged | **[[OnPushableMovementTypeChanged]]**  |
| FOnPushableProgressUpdated | **[[OnPushableProgressUpdated]]**  |
| FOnPushableReachedEndPoint | **[[OnPushableReachedEndPoint]]**  |
| USkeletalMeshComponent * | **[[OwnerSiegeMesh]]**  |
| TArray< UAkAudioEvent * > | **[[PlayMovingSounds]]**  |
| [FReplicated_Bool](/docs/SDK/Source/Classes/structFReplicated__Bool.md) | **[[PushableActive]]**  |
| [FPushableComponentProperties](/docs/SDK/Source/Classes/structFPushableComponentProperties.md) | **[[PushableComponentProperties]]**  |
| TArray< [FPushableEndPoint](/docs/SDK/Source/Classes/structFPushableEndPoint.md) > | **[[PushableEndPoints]]**  |
| EPushableMovementType | **[[PushableMovementType]]**  |
| float | **[[PushableProgress]]**  |
| [FReplicated_Float_FullPrecision](/docs/SDK/Source/Classes/structFReplicated__Float__FullPrecision.md) | **[[PushableProgressAuthority]]**  |
| UPrimitiveComponent * | **[[PushingCollisionComponent]]**  |
| [FDataTableRowSelection](/docs/SDK/Source/Classes/structFDataTableRowSelection.md) | **[[PushingCompleteScoreEvent]]**  |
| [FDataTableRowSelection](/docs/SDK/Source/Classes/structFDataTableRowSelection.md) | **[[PushingIntervalScoreEvent]]**  |
| [FReplicated_FFollowerPushableComponentProperties](/docs/SDK/Source/Classes/structFReplicated__FFollowerPushableComponentProperties.md) | **[[ReplicatedFollowerPushableComponentProperties]]**  |
| [FReplicated_FollowerPushables](/docs/SDK/Source/Classes/structFReplicated__FollowerPushables.md) | **[[ReplicatedFollowerPushables]]**  |
| [FReplicated_UInt8](/docs/SDK/Source/Classes/structFReplicated__UInt8.md) | **[[ReplicatedMovementState]]**  |
| [FReplicated_FPushableComponentProperties](/docs/SDK/Source/Classes/structFReplicated__FPushableComponentProperties.md) | **[[ReplicatedPushableComponentProperties]]**  |
| [FReplicatedArray_PushableEndPoints](/docs/SDK/Source/Classes/structFReplicatedArray__PushableEndPoints.md) | **[[ReplicatedPushableEndPoints]]**  |
| [FReplicated_EPushableMovementType](/docs/SDK/Source/Classes/structFReplicated__EPushableMovementType.md) | **[[ReplicatedPushableMovementType]]**  |
| [FReplicated_AActorPtr](/docs/SDK/Source/Classes/structFReplicated__AActorPtr.md) | **[[ReplicatedSplineActor]]**  |
| [FReplicated_Float](/docs/SDK/Source/Classes/structFReplicated__Float.md) | **[[ReplicatedTimeToCompleteSeconds]]**  |
| [APushableSplineActor](/docs/SDK/Source/Classes/classAPushableSplineActor.md) * | **[[SplineActor]]**  |
| USplineComponent * | **[[SplineComponent]]**  |
| float | **[[StartingDistance]]**  |
| [UStatsComponent](/docs/SDK/Source/Classes/classUStatsComponent.md) * | **[[StatsComponent]]**  |
| TArray< UAkAudioEvent * > | **[[StopMovingSounds]]**  |
| [UTeamCapturePointComponent](/docs/SDK/Source/Classes/classUTeamCapturePointComponent.md) * | **[[TeamCapturePointComponent]]**  |
| float | **[[TimeToCompleteSeconds]]**  |
| bool | **[[bAllowDisableOfPhysicsForOneTick]]**  |
| bool | **[[bCanBeBasedWhilePushable]]**  |
| bool | **[[bDisablePawnCollisionOnSkeletalMeshWhenActive]]**  |
| bool | **[[bShowHudProgressForCurrentSplineSegment]]**  |
| bool | **[[bTeleportWithPhysics]]**  |
| bool | **[[bTestExperimentalTeleport]]**  |
| bool | **[[bUpdateMarkerWithHealth]]**  |
| bool | **[[bUpdateMarkerWithProgress]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200