# VISION TRANSFORMER WITH ASSOCIATION DISCREPANCY FOR ANOMALY DETECTION
*Authors - Shuo Zhang, Jing Liu∗

**Abstract**- *Visual anomaly detection and localization are essential tasks in many safety-critical real-world scenarios. Our approach involves a transformer network with an association discrepancy, combining elements of patch embedding and a reconstruction-based method. We find it difficult to capture rich associations from abnormal patches to the entire image because anomalies primarily focus on their adjacent patches. However, the nontrivial associations between normal patches and the entire image can be easily expressed by the
self-attention weights of each patch. We use a minimax strategy to amplify this association discrepancy, inherently distinguishing between normal and abnormal patches and preserving the positional information of the split patches, which is then processed by a Gaus-
sian mixture density network to pinpoint the regions of anomalies. Extensive experiments conducted on the industrial inspection dataset demonstrate that the proposed method significantly improves visual anomaly detection and localization performance compared to the competing methods.*

# Network
The network is inspired from [Vision Transformer](https://openreview.net/pdf?id=YicbFdNTTy). 
It adapts the trasnformer network for image anomaly detection and localization.
<div align=center>
<img src="image/vit.png">
<img src="image/result.png">
<\div>

