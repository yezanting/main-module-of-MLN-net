# MLN-NET-VERSON1

## MLN-net: A multi-source medical image segmentation method for clustered microcalcifications using multiple layer normalization

**Abstract**
The accurate segmentation of clustered microcalcifications in mammography is crucial for the diagnosis and treatment of breast cancer. Despite exhibiting expert-level accuracy, recent deep learning advancements in 
medical image segmentation provide insufficient contribution to practical applications, due to the domain shift resulting from differences in patient postures, individual gland density, and imaging modalities, etc. 
In this paper, a novel framework named MLN-net is proposed for clustered microcalcification segmentation. It can accurately segment multi-source images using only single source images. Specifically, to rich domain 
distribution information, we introduce a source domain image augmentation for generating multi-source images. A structure of multiple layer normalization (LN) layers is then used to construct the segmentation 
network, which can be found efficient for clustered microcalcification segmentation in different domains. Additionally, a branch selection strategy is designed for measuring the similarity of the source domain data 
and the target domain data. To validate the proposed MLN-net, extensive analyses including ablation experiments are performed, comparison of 12 baseline methods. MLN-net enhances segmentation quality of full-field 
digital mammography (FFDM) and digital breast tomosynthe (DBT) images from the FFDM-DBT dataset, achieving the average Dice similarity coefficient (DSC) of 86.52% and the average Hausdorff distance (HD) of 20.49mm 
on the source domain DBT. And it outperforms the baseline models for the task in FFDM images from both the CBIS-DDSM and FFDM-DBT dataset, achieving the average DSC of 50.78% and the average HD of 35.12mm on 
the source domain CBIS-DDSM. Extensive experiments validate the effectiveness of MLN-net in segmenting clustered microcalcifications from different domains and its segmentation accuracy surpasses state-of-the-art 
methods.


## Data
We use FFDM-DBT and CBIS-DDSM dataset to validate the proposed MLN-net. FFDM-DBT is private dataset, and due to privacy concerns, we only show a portion of the data as toy-data to show its data characteristics.
CBIS-DDSM can be obtained from the [website](https://aistudio.baidu.com/datasetdetail/37567).


## Main modules
We have open-sourced MLN-net's main modules' code in Version1, including the source domain data augmentation module, the multi-LN structure and the branch selection strategy. 
The backbone of MLN-net comes from [Swinunet](https://github.com/HuCaoFighting/Swin-Unet). The complete code is being collated and will be released soon.


## Acknowledgements

Our codes are built upon [CSDG](https://github.com/cheng-01037/Causality-Medical-Image-Domain-Generalization), 
[Swinunet](https://github.com/HuCaoFighting/Swin-Unet), and [Dual-Normalization](https://github.com/zzzqzhou/Dual-Normalization), thanks for their contribution to the community and the development of researches!
