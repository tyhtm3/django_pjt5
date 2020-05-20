# 영화 추천

`requirements.txt`

```bash
backcall==0.1.0
beautifulsoup4==4.9.1
bootstrap4==0.1.0
colorama==0.4.3
decorator==4.4.2
Django==2.1.15
django-bootstrap-pagination==1.7.1
django-bootstrap4==1.1.1
django-extensions==2.2.9
djangorestframework==3.11.0
ipython==7.14.0
ipython-genutils==0.2.0
jedi==0.17.0
parso==0.7.0
pickleshare==0.7.5
prompt-toolkit==3.0.5
Pygments==2.6.1
pytz==2020.1
six==1.14.0
soupsieve==2.0.1
traitlets==4.3.3
wcwidth==0.1.9

```



**추천 알고리즘** 

- 이전에 좋아요 눌렀던 영화 기준

- 랜덤 

  ```python
  #views.py
  @api_view(['GET'])
  def recommend(request):
      if len(request.user.like_movies.values('genres')) ==0 :
      ## 다른거 좋아요 누른 적 있으면 같은 장르.
          temp = datetime.now().second % 19
          print(temp)
          arr= [10770,10752,10751,10749,10402,9648,878,99,80,53,37,36,35,28,27,18,16,14,12]
          genre = get_object_or_404(Genre, pk=arr[temp])
      else:
          genre_id = request.user.like_movies.values('genres').annotate(count=Count('genres'))[0].get('genres')
          genre = get_object_or_404(Genre, pk = genre_id)
      movies =Movie.objects.filter(genres=genre)
      serializer = MovieSerializer(movies, many =True)
  
      return Response(serializer.data)
  ```

  ```html
  //movie_list.html
  
  <script>
      document.querySelectorAll('.like').forEach(item=>{
          item.addEventListener('click', event=>{
              const movieId = event.target.dataset.articleId
              axios.get(`/movies/${movieId}/like/`)
                  .then(res=>{
                      const count = res.data.count
                      const flag = res.data.flag 
                      if(flag){
                          document.querySelector('.like').setAttribute('style', 'color:crimson')
                      }else{
                          document.querySelector('.like').setAttribute('style', 'color:black')
  
                      }
                      document.querySelector(`#like-count-${movieId}`).innerText = count
                  })
          })
      })
  </script>
  
  ```

  



**느낀점**

-  디자인은 나의 길이 아니다. 나는 Backend에 뼈를 묻어야 겠다.  -재영-
-  지금까지 배운거 거의 다 써먹어 봐서 유익한 시간이었다. -재영 - 

-  아직 미숙하다는 것을 느꼈습니다. -선민-

-  vscode extension은 너무 좋다. 짱이다. -선민-

**특히 어려웠던 점**

- 오늘 백지 코딩을 시도해 봤는데, 생각보다 어려웠습니다. -재영-
- Ajax 쓰는게 어려웠습니다. -선민- 



**향후 개선 사항**

- 추천 알고리즘 보수
- Front Design....

