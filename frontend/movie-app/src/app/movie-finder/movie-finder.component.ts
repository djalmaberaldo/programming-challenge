import { Component, OnInit } from '@angular/core';
import { MovieService } from './movie-finder.service.component';
import { IMovie } from './movie.model';
import { HttpErrorResponse, HttpResponse } from '@angular/common/http';

@Component({
  selector: 'app-movie-finder',
  templateUrl: './movie-finder.component.html',
  styleUrls: ['./movie-finder.component.scss']
})
export class MovieFinderComponent implements OnInit {

  movies: IMovie[];
  message: any;
  search = '';
  filterBy = 'primaryTitle';

  constructor(
    private movieService: MovieService
  ) { }

  ngOnInit() {
    this.loadMovies();
  }

  loadMovies() {
    this.movieService
    .query({filterBy: this.filterBy, search: this.search})
    .subscribe(
      (res: HttpResponse<IMovie[]>) => (this.movies = res.body["data"]),
      (res: HttpErrorResponse) => console.log(res.message)
    );
  }

 
}
