---
title: UTBLGameplayDebuggingComponent
type: class
aliases: UTBLGameplayDebuggingComponent
share: false

---

# UTBLGameplayDebuggingComponent





Inherits from UActorComponent

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| | **[[UTBLGameplayDebuggingComponent]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< [FBonesDebugInfo](/docs/SDK/Source/Classes/structFBonesDebugInfo.md) > | **[[BonesDebugInfo]]**  |
| TArray< FName > | **[[BonesDebugNames]]**  |
| [FDesyncDebugInfo](/docs/SDK/Source/Classes/structFDesyncDebugInfo.md) | **[[ClientDesyncDebugInfo]]**  |
| TArray< FName > | **[[DebugCategories]]**  |
| [FDebugProjectileHit](/docs/SDK/Source/Classes/structFDebugProjectileHit.md) | **[[DebugProjectileHit]]**  |
| TArray< [UTBLComponent](/docs/SDK/Source/Classes/classUTBLComponent.md) * > | **[[DebuggingComponents]]**  |
| [FDesyncDebugInfo](/docs/SDK/Source/Classes/structFDesyncDebugInfo.md) | **[[DesyncDebugInfo]]**  |
| TArray< [FAbilityInvocationDebugInfo](/docs/SDK/Source/Classes/structFAbilityInvocationDebugInfo.md) > | **[[InvocationDebugInfo]]**  |
| TArray< [FPhysicsDebugInfo](/docs/SDK/Source/Classes/structFPhysicsDebugInfo.md) > | **[[PhysicsDebugInfo]]**  |
| TArray< [FPropertyDebugInfo](/docs/SDK/Source/Classes/structFPropertyDebugInfo.md) > | **[[PropertyDebugInfo]]**  |
| [FReplicationDebugInfo](/docs/SDK/Source/Classes/structFReplicationDebugInfo.md) | **[[ReplicationDebugInfo]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200