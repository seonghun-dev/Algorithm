/*
 * 제목 : 신규 아이디 추천 프로그램 작성
 * 링크 : https://programmers.co.kr/learn/courses/30/lessons/72410
 * 코딩테스트연습 > 2021 KAKAO BLIND RECRUITMENT > 신규아이디추천
 * */

#include <stdio.h>
#include <string.h>
#include "DLinkedList.h"


int main() {
///// List의 생성 및 초기화
    List list;
    int data;
    ListInit(&list);
    char scanstr[1000];
    scanf("%s",scanstr);


/////1단계 모든 대문자를 소문자로 변경하며 문자열 배열을 연결 리스트로 변경
    int sizeofstr = strlen(scanstr); //문자열이 들어 있는 배열의 끝 번호 확인
    for (; sizeofstr > 0; sizeofstr--) { //Linked List에서는 head부터 데이터가 입력되기 때문에 배열의 끝부터 처음으로 역순으로 넣어준다.
        if (scanstr[sizeofstr - 1] >= 'A' && scanstr[sizeofstr - 1] <= 'Z') //new_id의 대문자 확인
            LInsert(&list, scanstr[sizeofstr - 1] + 32); //LinkedList가 먼저 생성하고 1단계의 값이 변경 된다.
        else
            LInsert(&list, scanstr[sizeofstr - 1]); //대문자가 아닐경우 역순으로 대입
    }


/////2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    if (LFirst(&list, &data)) {
        (data >= 48 && data <= 57) || (data >= 97 && data <= 122) || data == 45 || data == 46 || data == 95 ? 0 : LRemove(&list);
        while (LNext(&list, &data))
        (data >= 48 && data <= 57) || (data >= 97 && data <= 122) || data == 45 || data == 46 || data == 95 ? 0 : LRemove(&list);
    }


/////3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
int tempcheckcon, k = 0;
    while (k <= 2001) {
        if (LFirst(&list, &data)) {
	    tempcheckcon = data;  //tempcheckcon에 전에 있던 값 담아서 확인
	    LNext(&list, &data);
	   (data == 46) && (data == tempcheckcon) ? LRemove(&list) : k++; //.이고 전에 있던 값고 같을 경우 삭제
            while (LNext(&list, &data)) {
                (data == 46) && (data == tempcheckcon) ? LRemove(&list) : k++;
		tempcheckcon = data;  //이동전 이전값 담음
            }
        } 
	else 
            break;
    }

/////3단게 추가 두번째 문자와 세번째 문자가 같은 경우(A..DA 같은 경우 처리)
    if(LFirst(&list, &data)){
	LNext(&list,&data);	tempcheckcon = data;	LNext(&list,&data);
	(data ==46) && (data == tempcheckcon) ? LRemove(&list) : 0;
    }

/////4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다
    if (LFirst(&list, &data)) {
        data == 46 ? LRemove(&list) : 0 ;
        while (LNext(&list, &data)) {}  //new_id 끝까지 이동
        data == 46 ? LRemove(&list) : 0 ;
    }

/////5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.=.= 의 경우 유의
    LFirst(&list, &data) == 0 ? LInsert(&list, 97) : 0 ;


/////6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
/////만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    while (list.numOfData > 15) {
        LFirst(&list, &data);       //list.numOfData>15이므로 바로 LFirst로 접근.
        while (LNext(&list, &data)) {} //LNext로 끝으로 이동.
        LRemove(&list);                 //끝 부분 삭제
    }

    if (LFirst(&list, &data)) {
        while (LNext(&list, &data)) {}
        data == 46 ? LRemove(&list) : 0 ;
    }


/////7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    while (list.numOfData <= 2) {
            LFirst(&list, &data);
            int temp = data;  //Lfirst data을 temp에 저장
            LRemove(&list);  //Lfirst삭제
            LNext(&list, &data); //data가 1개일 경우 0반환 data에 Lfirst값 2일 경우에 다음 데이터 이동 
            LInsert(&list, data); //2일 경우 앞에 Lnext데이터 추가
            LInsert(&list, temp);  //2일 경우 Lfirst값 맨 앞에 추가
    }	

/////연결리스트 값 출력
    LFirst(&list, &data);
    printf("%c", data);
    while (LNext(&list, &data))
            printf("%c", data);
    printf("\n");

    return 0;
}
