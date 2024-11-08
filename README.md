# Diagnostic-des-maladies-pulmonaires-incluant-le-COVID-19-CNN
A healthcare management system using Spring Boot for backend, JavaFX for UI, and Hugging Face for AI-powered chat. It includes RMI for component communication, MySQL for data storage, and Deep Learning (CNNs) to detect lung diseases from X-ray images, improving diagnosis and patient management.

**Project Title**: Detection of Pulmonary Diseases Including COVID-19 Using CNN

Health plays a vital role in individual and collective well-being, encompassing the diagnosis, treatment, and prevention of diseases, as well as the promotion of healthy lifestyles. A well-structured healthcare system, composed of organizations, professionals, and institutions, provides essential medical services to the public. Public health institutions, in particular, are crucial in promoting health, preventing disease outbreaks, and encouraging healthy behaviors.

**Technologies in Medical Imaging**

Medical technologies, such as **radiology**, allow for precise diagnostics by visualizing internal structures. In the past two years, the COVID-19 pandemic has profoundly impacted daily life. The rapid spread of the virus, combined with its severe effects on older adults and those with chronic lung diseases, has placed significant pressure on healthcare facilities and medical personnel. With the growing demand for diagnostics and a shortage of PCR and serology tests, **chest X-rays** have become an invaluable tool for reducing diagnostic uncertainty.

**Commonly Used Technologies for Disease Diagnosis**

Several technologies are widely used for diagnosing diseases, including:

- **Laboratory Tests**: Analyze blood, urine, or other bodily fluids to detect diseases.
- **Radiology**: Uses imaging tools like **X-rays**, **CT scans**, and **MRI** to visualize internal structures.
- **Endoscopy**: Inserts a small camera into the body to examine internal areas.
- **Biopsies**: Extract tissue samples for examination under a microscope.
- **Genetic Tests**: Analyze DNA to identify mutations associated with specific conditions.
- **Electronic Health Records (EHR)**: Digital records of an individual's medical history to aid in diagnosis and treatment.
- **Artificial Intelligence (AI) and Machine Learning (ML)**: Analyze medical data to assist in diagnosis and treatment planning.

**Advancements in Medical Imaging and Deep Learning**

Medical imaging has transformed healthcare through advanced image processing techniques. **Deep Learning**, particularly **Convolutional Neural Networks (CNNs)**, is widely used for detecting conditions such as tumors, prostate cancer, lung nodules, and breast cancer. Research efforts have leveraged CNN models for identifying COVID-19 from chest X-ray images.

This study focuses on analyzing chest X-rays to detect pulmonary diseases, including COVID-19. **Convolutional Neural Networks** and **histogram equalization** are utilized to identify lung abnormalities. By integrating **AI** and **Machine Learning**, our approach aims to improve diagnostic accuracy, providing healthcare professionals with efficient tools for detecting and managing lung diseases.

**Project Overview**

In this project, we developed a lightweight CNN model based on deep learning, utilizing the **COVID-QU** lung X-ray dataset. Key steps include:

1. **Image Preprocessing**: We applied histogram equalization to balance image intensity.
2. **Dataset Splitting**: The dataset was divided into training and testing subsets.
3. **CNN Implementation**: A CNN architecture was implemented to detect COVID-19 or other pulmonary diseases from chest X-rays.

This approach assists medical personnel in quickly assessing patient conditions, thereby minimizing health risks.

**Structure of the Report**

The project is organized into four main chapters:

1. **Definitions and Basic Concepts**: Introduces fundamental concepts related to medical image processing.
2. **Current State of Image Processing Techniques for Pulmonary Disease Detection**: Examines existing methods for identifying lung diseases using imaging.
3. **Project Overview**: Outlines the project objectives, context, and scope.
4. **Deep Learning-Based Image Processing Methodology**: Details the development of a deep learning approach for analyzing medical images.
