---
title: APushableSiegeActor
type: class
aliases: APushableSiegeActor
share: false

---

# APushableSiegeActor





Inherits from [ATBLActor](/docs/SDK/Source/Classes/classATBLActor.md), [IHUDMarkerInterface](/docs/SDK/Source/Classes/classIHUDMarkerInterface.md), AActor, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[APushableSiegeActor]]**() |
| void | **[[AddLogEntry]]**(const FString & LogEntry) |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| void | **[[SetAvoidanceEnabled]]**(bool bEnable) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[OnMeshLODChanged]]**() |
| void | **[[OnPushableActivated]]**(bool bIsActive) |
| void | **[[OnPushableCompleted]]**() |
| void | **[[OnPushableReachedEndPoint]]**(int32 EndPointNum, [FPushableEndPoint](/docs/SDK/Source/Classes/structFPushableEndPoint.md) EndPoint, bool IsLastEndPoint) |
| void | **[[OnRep_ReplicatedSiegeState]]**() |
| void | **[[SetSiegeState]]**(ESiegeActorState NewState) |
| void | **[[SiegeStateAnimationUpdated]]**(ESiegeActorState NewState) |
| void | **[[UpdateSkeletalMesh]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| USceneComponent * | **[[DefaultSceneComponent]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| UAkComponent * | **[[AudioComponent]]**  |
| FNavAvoidanceMask | **[[AvoidanceGroup]]**  |
| float | **[[AvoidanceHeight]]**  |
| FVector | **[[AvoidanceLocation]]**  |
| int32 | **[[AvoidanceUID]]**  |
| USceneComponent * | **[[HudMarkerComponentLocation]]**  |
| [UHudMarkerDisplayComponent](/docs/SDK/Source/Classes/classUHudMarkerDisplayComponent.md) * | **[[HudMarkerDisplay]]**  |
| int32 | **[[LowLodPhysAssetLevel]]**  |
| UBoxComponent * | **[[PawnPushingCollisionComponent]]**  |
| FOnPushableCompleted | **[[PushableComplete]]**  |
| [UPushableComponent](/docs/SDK/Source/Classes/classUPushableComponent.md) * | **[[PushableComponent]]**  |
| UPhysicsAsset * | **[[PushablePhysAsset]]**  |
| UPhysicsAsset * | **[[PushablePhysAssetLowLod]]**  |
| FOnPushableReachedEndPoint | **[[PushableReachedEndPoint]]**  |
| [UPushingComponent](/docs/SDK/Source/Classes/classUPushingComponent.md) * | **[[PushingComponent]]**  |
| [FReplicated_UInt8](/docs/SDK/Source/Classes/structFReplicated__UInt8.md) | **[[ReplicatedSiegeState]]**  |
| USkeletalMeshComponent * | **[[SiegeMesh]]**  |
| UPhysicsAsset * | **[[StationaryPhysAsset]]**  |
| UPhysicsAsset * | **[[StationaryPhysAssetLowLod]]**  |
| [UTBLNavModifierComponent](/docs/SDK/Source/Classes/classUTBLNavModifierComponent.md) * | **[[TBLNavModifier]]**  |
| [UTeamCapturePointComponent](/docs/SDK/Source/Classes/classUTeamCapturePointComponent.md) * | **[[TeamCapturePoint]]**  |
| bool | **[[bDedicatedServerUseLowLodPhysics]]**  |
| bool | **[[bUseRVOAvoidance]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200