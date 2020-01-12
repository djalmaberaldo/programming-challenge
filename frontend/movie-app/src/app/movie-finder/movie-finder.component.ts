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

  constructor(
    private movieService: MovieService
  ) { }

  ngOnInit() {
    this.loadMovies();
  }

  loadMovies() {
    this.movieService
    .query({})
    .subscribe(
      (res: HttpResponse<IMovie[]>) => (this.movies = res.body["data"]),
      (res: HttpErrorResponse) => this.exportMessage(res.message)
    );
  }

  exportMessage(message) {
    console.log(message);
  }
}
