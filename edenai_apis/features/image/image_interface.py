from abc import abstractmethod
from io import BufferedReader
from typing import Literal, Optional, Dict, Any

from edenai_apis.features.image.anonymization.anonymization_dataclass import (
    AnonymizationDataClass,
)
from edenai_apis.features.image.automl_classification.create_project_async.automl_classification_create_project_async_dataclass import (
    AutomlClassificationCreateProjectDataClass,
)
from edenai_apis.features.image.automl_classification.delete_project_async.automl_classification_delete_project_async_dataclass import (
    AutomlClassificationDeleteProjectDataClass,
)
from edenai_apis.features.image.automl_classification.predict_async.automl_classification_predict_async_dataclass import (
    AutomlClassificationPredictDataClass,
)
from edenai_apis.features.image.automl_classification.train_async.automl_classification_train_async_dataclass import (
    AutomlClassificationTrainDataClass,
)
from edenai_apis.features.image.automl_classification.upload_data_async.automl_classification_upload_data_async_dataclass import (
    AutomlClassificationUploadDataDataClass,
)
from edenai_apis.features.image.background_removal import BackgroundRemovalDataClass
from edenai_apis.features.image.embeddings.embeddings_dataclass import (
    EmbeddingsDataClass,
)
from edenai_apis.features.image.explicit_content.explicit_content_dataclass import (
    ExplicitContentDataClass,
)
from edenai_apis.features.image.face_compare.face_compare_dataclass import (
    FaceCompareDataClass,
)
from edenai_apis.features.image.face_detection.face_detection_dataclass import (
    FaceDetectionDataClass,
)
from edenai_apis.features.image.face_recognition.add_face.face_recognition_add_face_dataclass import (
    FaceRecognitionAddFaceDataClass,
)
from edenai_apis.features.image.face_recognition.create_collection.face_recognition_create_collection_dataclass import (
    FaceRecognitionCreateCollectionDataClass,
)
from edenai_apis.features.image.face_recognition.delete_collection.face_recognition_delete_collection_dataclass import (
    FaceRecognitionDeleteCollectionDataClass,
)
from edenai_apis.features.image.face_recognition.delete_face.face_recognition_delete_face_dataclass import (
    FaceRecognitionDeleteFaceDataClass,
)
from edenai_apis.features.image.face_recognition.list_collections.face_recognition_list_collections_dataclass import (
    FaceRecognitionListCollectionsDataClass,
)
from edenai_apis.features.image.face_recognition.list_faces.face_recognition_list_faces_dataclass import (
    FaceRecognitionListFacesDataClass,
)
from edenai_apis.features.image.face_recognition.recognize.face_recognition_recognize_dataclass import (
    FaceRecognitionRecognizeDataClass,
)
from edenai_apis.features.image.generation.generation_dataclass import (
    GenerationDataClass,
)
from edenai_apis.features.image.landmark_detection.landmark_detection_dataclass import (
    LandmarkDetectionDataClass,
)
from edenai_apis.features.image.logo_detection.logo_detection_dataclass import (
    LogoDetectionDataClass,
)
from edenai_apis.features.image.object_detection.object_detection_dataclass import (
    ObjectDetectionDataClass,
)
from edenai_apis.features.image.question_answer import QuestionAnswerDataClass
from edenai_apis.features.image.search.get_image.search_get_image_dataclass import (
    SearchGetImageDataClass,
)
from edenai_apis.features.image.search.get_images.search_get_images_dataclass import (
    SearchGetImagesDataClass,
)
from edenai_apis.features.image.search.search_dataclass import SearchDataClass
from edenai_apis.utils.types import (
    ResponseSuccess,
    ResponseType,
    AsyncLaunchJobResponseType,
    AsyncBaseResponseType,
    AsyncResponseType,
)


class ImageInterface:
    @abstractmethod
    def image__anonymization(
        self, file: BufferedReader
    ) -> ResponseType[AnonymizationDataClass]:
        """
        Anonymize face, names, car plates etc. from an image

        Args:
            file (BufferedReader): image to anonymize
        """
        raise NotImplementedError

    @abstractmethod
    def image__embeddings(
        self,
        file: str,
        representation: str,
        file_url: str = "",
        model: Optional[str] = None,
    ) -> ResponseType[EmbeddingsDataClass]:
        """
        Embeds an image

        Args:
            file (BufferedReader): image to analyze
            model (str): which ai model to use, default to `None`
            representation (str): type of embedding representation
        """
        raise NotImplementedError

    @abstractmethod
    def image__explicit_content(
        self, file: str, file_url: str = ""
    ) -> ResponseType[ExplicitContentDataClass]:
        """
        Detect explicit content in an image

        Args:
            file (BufferedReader): image to analyze
        """
        raise NotImplementedError

    @abstractmethod
    def image__face_detection(
        self, file: str, file_url: str = ""
    ) -> ResponseType[FaceDetectionDataClass]:
        """
        Detect faces in an image

        Args:
            file (BufferedReader): image to analyze
        """
        raise NotImplementedError

    @abstractmethod
    def image__landmark_detection(
        self, file: str, file_url: str = ""
    ) -> ResponseType[LandmarkDetectionDataClass]:
        """
        Detect popular landmark in an image
        (eg: popular tourist spots like Eiffel Tower)

        Args:
            file (BufferedReader): image to analyze
        """
        raise NotImplementedError

    @abstractmethod
    def image__logo_detection(
        self, file: str, file_url: str = ""
    ) -> ResponseType[LogoDetectionDataClass]:
        """
        Detect Logo in an image

        Args:
            file (BufferedReader): image to analyze
        """
        raise NotImplementedError

    @abstractmethod
    def image__object_detection(
        self,
        file: str,
        file_url: str = "",
        model: str = None,
    ) -> ResponseType[ObjectDetectionDataClass]:
        """
        Detect objects in an image

        Args:
            file (BufferedReader): image to analyze
        """
        raise NotImplementedError

    @abstractmethod
    def image__question_answer(
        self,
        file: str,
        temperature: float,
        max_tokens: int,
        file_url: str = "",
        model: Optional[str] = None,
        question: Optional[str] = None,
    ) -> ResponseType[QuestionAnswerDataClass]:
        """
        Ask question related to given image and get an answer

        Args:
            file (BufferedReader): image to analyze
            question (str): your query
            maximum_tokens (int): maximum number of tokens to be generated
            model (str): which ai model to use, default to 'None'
        """
        raise NotImplementedError

    @abstractmethod
    def image__search__create_project(self, project_name: str) -> str:
        """
        Create an image search project

        Args:
            file (BufferedReader): image to analyze
        """
        raise NotImplementedError

    ## TO DO better response types for image search
    @abstractmethod
    def image__search__upload_image(
        self, file: str, image_name: str, project_id: str, file_url: str = ""
    ) -> ResponseSuccess:
        """
        Upload image for an image search project

        Args:
            file (BufferedReader): image to analyze
            image_name (str): name of the image
            project_id (str): image search project id
        """
        raise NotImplementedError

    @abstractmethod
    def image__search__delete_image(
        self, image_name: str, project_id: str
    ) -> ResponseSuccess:
        """
        Delete image of an image search project

        Args:
            image_name (str): name of the image
            project_id (str): image search project id
        """
        raise NotImplementedError

    @abstractmethod
    def image__search__get_images(
        self, project_id: str
    ) -> ResponseType[SearchGetImagesDataClass]:
        """
        get images of an image search project

        Args:
            project_id (str): image search project id
        """
        raise NotImplementedError

    @abstractmethod
    def image__search__get_image(
        self, image_name: str, project_id: str
    ) -> ResponseType[SearchGetImageDataClass]:
        """
        get image of an image search project

        Args:
            image_name (str): name of the image
            project_id (str): image search project id
        """
        raise NotImplementedError

    @abstractmethod
    def image__search__launch_similarity(
        self, file: str, project_id: str, file_url: str = ""
    ) -> ResponseType[SearchDataClass]:
        """
        Launch similarity analysis of a search image project

        Args:
            file (BufferedReader): image to analyze
            project_id (str): image search project id
        """
        raise NotImplementedError

    @abstractmethod
    def image__face_recognition__create_collection(
        self, collection_id: str
    ) -> FaceRecognitionCreateCollectionDataClass:
        """
        Create a Face Collection to analyze for face recognition

        Args:
            collection_id (str): ID given to created collection
        """
        raise NotImplementedError

    @abstractmethod
    def image__face_recognition__list_collections(
        self,
    ) -> ResponseType[FaceRecognitionListCollectionsDataClass]:
        """
        List all Face Collections
        """
        raise NotImplementedError

    @abstractmethod
    def image__face_recognition__list_faces(
        self, collection_id: str
    ) -> ResponseType[FaceRecognitionListFacesDataClass]:
        """
        List a Faces of a Collection

        Args:
            collection_id (str): ID of collection
        """
        raise NotImplementedError

    @abstractmethod
    def image__face_recognition__delete_collection(
        self, collection_id: str
    ) -> ResponseType[FaceRecognitionDeleteCollectionDataClass]:
        """
        Delete a Face Collection

        Args:
            collection_id (str): ID of collection
        """
        raise NotImplementedError

    @abstractmethod
    def image__face_recognition__add_face(
        self, collection_id: str, file: str, file_url: str = ""
    ) -> ResponseType[FaceRecognitionAddFaceDataClass]:
        """
        Detect and add a face to a collection from an image

        Args:
            collection_id (str): ID of collection
            file (BufferedReader): image to analyze
        """
        raise NotImplementedError

    @abstractmethod
    def image__face_recognition__delete_face(
        self, collection_id, face_id
    ) -> ResponseType[FaceRecognitionDeleteFaceDataClass]:
        """
        Delete a face from collection

        Args:
            collection_id (str): ID of collection
            face_id (str): ID of face to delete
        """
        raise NotImplementedError

    @abstractmethod
    def image__face_recognition__recognize(
        self, collection_id: str, file: str, file_url: str = ""
    ) -> ResponseType[FaceRecognitionRecognizeDataClass]:
        """
        Detect the biggers face from image and try
        to find faces from the same person in the face collection

        Args:
            collection_id (str): ID of collection
            file (BufferedReader): image to analyze
        """
        raise NotImplementedError

    @abstractmethod
    def image__generation(
        self,
        text: str,
        resolution: Literal["256x256", "512x512", "1024x1024"],
        num_images: int = 1,
        model: Optional[str] = None,
    ) -> ResponseType[GenerationDataClass]:
        """
        Generate an image based on a text prompt.

        Args:
            text(str): prompt of the image to generate
        """
        raise NotImplementedError

    @abstractmethod
    def image__face_compare(
        self,
        file1: str,
        file2: str,
        file1_url: str,
        file2_url: str,
    ) -> ResponseType[FaceCompareDataClass]:
        """

        Args:
            file1 (str): _description_
            file2 (str): _description_
            file1_url (str): _description_
            file2_url (str): _description_
        """
        raise NotImplementedError

    @abstractmethod
    def image__background_removal(
        self,
        file: str,
        file_url: str = "",
        provider_params: Optional[Dict[str, Any]] = None,
    ) -> ResponseType[BackgroundRemovalDataClass]:
        """
        Remove background from an image.
        Each provider has its own parameters

        Args:
            file (str): Image to analyze
            file_url (str): Url of the image to analyze
            provider_params (dict): Provider specific parameters for the request.

        Returns:
            ResponseType[BackgroundRemovalDataClass]
        """
        raise NotImplementedError

    @abstractmethod
    def image__automl_classification__create_project(
        self, name: Optional[str] = None
    ) -> ResponseType[AutomlClassificationCreateProjectDataClass]:
        """
        Create an automl classification project/dataset.

        Args:
            name (str): Name of the project/dataset

        Returns:
            AsyncLaunchJobResponseType
        """
        raise NotImplementedError

    @abstractmethod
    def image__automl_classification__upload_data_async__launch_job(
        self,
        project_id: str,
        label: str,
        type_of_data: str,
        file: str,
        file_url: str = "",
    ) -> AsyncLaunchJobResponseType:
        """
        Upload image to dataset

        Args:
            project_id (str): id of project
            label (str): label of the data
            type_of_data (str): type of data (train, test)
            file (str): image to upload
            file_url (str): url of the image to upload
        """
        raise NotImplementedError

    @abstractmethod
    def image__automl_classification__upload_data_async__get_job_result(
        self, provider_job_id: str
    ) -> AsyncBaseResponseType[AutomlClassificationUploadDataDataClass]:
        """
        Get the result of an asynchronous job by its ID

        Args:
            provider_job_id (str): id of async job
        """
        raise NotImplementedError

    @abstractmethod
    def image__automl_classification__train_async__launch_job(
        self, project_id: str
    ) -> AsyncLaunchJobResponseType:
        """
        Start training of automl classification model

        Args:
            project_id (str): id of project
        """
        raise NotImplementedError

    @abstractmethod
    def image__automl_classification__train_async__get_job_result(
        self, provider_job_id: str
    ) -> AsyncBaseResponseType[AutomlClassificationTrainDataClass]:
        """
        Get the result of an asynchronous job by its ID

        Args:
            provider_job_id (str): id of async job
        """
        raise NotImplementedError

    @abstractmethod
    def image__automl_classification__predict_async__launch_job(
        self, project_id: str, file: str, file_url: str = ""
    ) -> AsyncLaunchJobResponseType:
        """
        Get the prediction of the model

        Args:
            project_id (str): id of the project
            file (str): image to get prediction from
            file_url (str): url of the image to get the prediction from
        """
        raise NotImplementedError

    @abstractmethod
    def image__automl_classification__predict_async__get_job_result(
        self, provider_job_id: str
    ) -> AsyncBaseResponseType[AutomlClassificationPredictDataClass]:
        """
        Get the result of an asynchronous job by its ID

        Args:
            provider_job_id (str): id of async job
        """
        raise NotImplementedError

    @abstractmethod
    def image__automl_classification__delete_project_async__launch_job(
        self, project_id: str
    ) -> AsyncLaunchJobResponseType:
        """
        Delete an automl classification project

        Args:
            project_id (str): id of the project
        """
        raise NotImplementedError

    @abstractmethod
    def image__automl_classification__delete_project_async__get_job_result(
        self, provider_job_id: str
    ) -> AsyncBaseResponseType[AutomlClassificationDeleteProjectDataClass]:
        """
        Get the result of an asynchronous job by its ID

        Args:
            provider_job_id (str): id of async job
        """
        raise NotImplementedError
