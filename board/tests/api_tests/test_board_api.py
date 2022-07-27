import json

from rest_framework.test import APIClient, APITestCase

from board.models import Board as BoardModel
from user.models import User as UserModel


class TestBoardAPI(APITestCase):
    """
    BoardView의 API를 검증하는 클래스
    """

    def test_get_board_list(self) -> None:
        """
        BoardView의 get 함수를 검증하는 함수
        """
        client = APIClient()
        user = UserModel.objects.create(
            username="won1", password="1234", nickname="won"
        )
        BoardModel.objects.create(title="title", content="content", author=user)

        client.force_authenticate(user=user)
        url = "/board/?page_num=1"
        response = client.get(url)
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["total_count"], 1)

    def test_when_is_user_is_unauthenticated_in_get_board_list(self) -> None:
        """
        BoardView의 get 함수를 검증하는 함수
        case : 로그인하지 않은 사용자가 조회하는 경우
        """
        client = APIClient()

        url = "/board/?page_num=1"
        response = client.get(url)
        result = response.json()

        self.assertEqual(401, response.status_code)
        self.assertEqual(
            result["detail"], "자격 인증데이터(authentication credentials)가 제공되지 않았습니다."
        )

    # def test_when_parameter_doesnot_exist_in_get_board_list(self) -> None:
    #     """
    #     BoardView의 get 함수를 검증하는 함수
    #     case : 빈파라미터를 넣은 경우
    #     """
    #     client = APIClient()
    #     user = UserModel.objects.create(
    #         username="won1", password="1234", nickname="won"
    #     )
    #     BoardModel.objects.create(title="title", content="content", author=user)

    #     client.force_authenticate(user=user)
    #     url = "/board/"
    #     response = client.get(url)
    #     result = response.json()
    #     print(result)

        # with self.assertRaises(TypeError)

    def test_post_board_content(self) -> None:
        """
        BoardView의 post 함수를 검증하는 함수
        """
        client = APIClient()
        user = UserModel.objects.create(
            username="won1", password="1234", nickname="won"
        )
        request_data = {"title": "title", "content": "content", "author": user.id}

        client.force_authenticate(user=user)
        url = "/board/"
        response = client.post(
            url, data=json.dumps(request_data), content_type="application/json"
        )
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["message"], "게시글이 생성되었습니다.")

    def test_when_is_user_is_unauthenticated_in_post_board_content(self) -> None:
        """
        BoardView의 post 함수를 검증하는 함수
        case : 로그인하지 않은 사용자가 post하는 경우
        """
        client = APIClient()
        request_data = {"title": "title", "content": "content"}

        url = "/board/"
        response = client.post(
            url, data=json.dumps(request_data), content_type="application/json"
        )
        result = response.json()

        self.assertEqual(401, response.status_code)
        self.assertEqual(
            result["detail"], "자격 인증데이터(authentication credentials)가 제공되지 않았습니다."
        )

    
    def test_put_board_content(self) -> None:
        """
        BoardView의 put 함수를 검증하는 함수
        """
        client = APIClient()
        user = UserModel.objects.create(
            username="won1", password="1234", nickname="won"
        )
        user_board = BoardModel.objects.create(
            title="title", content="content", author=user
        )
        request_data = {"title": "수정된 제목", "content": "수정된 내용", "author": user.id}

        client.force_authenticate(user=user)
        url = "/board/" + str(user_board.id)
        response = client.put(
            url, data=json.dumps(request_data), content_type="application/json"
        )
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["message"], "게시글이 수정되었습니다.")
        
    
    def test_when_unauthenticated_user_put_board_content(self) -> None:
        """
        BoardView의 put 함수를 검증하는 함수
        case : 로그인하지 않은 사용자가 put하는 경우
        """
        
        client = APIClient()
        user = UserModel.objects.create(
            username="won1", password="1234", nickname="won"
        )
        user_board = BoardModel.objects.create(
            title="title", content="content", author=user
        )
        request_data = {"title": "수정된 제목", "content": "수정된 내용", "author": user.id}

        
        url = "/board/" + str(user_board.id)
        response = client.put(
            url, data=json.dumps(request_data), content_type="application/json"
        )
        result = response.json()
        print(result)

        self.assertEqual(401, response.status_code)
        self.assertEqual(
            result["detail"], "자격 인증데이터(authentication credentials)가 제공되지 않았습니다."
        )
    
    
    def test_when_user_is_not_author_in_put_board_content(self) -> None:
        """
        BoardView의 put 함수를 검증하는 함수
        case : 게시물을 쓴 사용자가 아닌 사람이 수정을 하려는 경우
        *원래 코드 수정 필요*
        """
        
        client = APIClient()
        user = UserModel.objects.create(
            username="won1", password="1234", nickname="won"
        )
        author = UserModel.objects.create(
            username="won2", password="1234", nickname="won2"
        )
        author_board = BoardModel.objects.create(
            title="title", content="content", author=author
        )
        request_data = {"title": "수정된 제목", "content": "수정된 내용", "author": author.id}

        client.force_authenticate(user=user)
        url = "/board/" + str(author_board.id)
        response = client.put(
            url, data=json.dumps(request_data), content_type="application/json"
        )
        result = response.json()

        #self.assertEqual(401, response.status_code)
        
        
            
    
