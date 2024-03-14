![[Pasted image 20230313201552.png]]


# 基础知识

## Blend Skinning
1. Skeleton subspace deformation methods——attach the surface of a mesh to an underlying skeletal structure.Each vertex in the mesh surface is transformed using a weighted influence of its neighboring bones. This influence can be defined linearly as in Linear Blend Skinning (LBS).
2. LBS: Linear blend skinning
     由于在这些行业中通常需要给 3D 模型做动画，比如我们用的是 5000 个顶点的人脸模型，这个人脸可以做 83 个表情，那么为了模拟这个人脸的各种表情我们就需要存储 5000\*83 个顶点的位置，非常的耗费空间。而线性蒙皮就是通过线性分解的方式将这些表情分解为多个由骨骼驱动的蒙皮动画，进而节约存储资源。
    ![[Pasted image 20230319140105.png|550]]
3. problem of LBS
     quaternion or dual-quaternion skinning, spherical skinning

## Auto-rigging

## Blend-shapes
