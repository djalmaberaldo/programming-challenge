import { Component, OnInit, Input } from '@angular/core';
import { IName } from '../movie-finder/movie.model';
import { MovieService } from '../movie-finder/movie-finder.service.component';
import { HttpResponse, HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-casting-box',
  templateUrl: './casting-box.component.html',
  styleUrls: ['./casting-box.component.scss']
})
export class CastingBoxComponent  {

  @Input() tconst: string;
  names = '';
  isSearching = false;

  constructor(
    private movieService: MovieService
  ) {}

  findName(identifier) {
    this.isSearching = true;
    this.movieService
      .findNames({
        tconst: identifier
      }).subscribe(
        (res: HttpResponse<IName[]>) => this.names = this.checkNameResult(res.body['data']),
        (res: HttpErrorResponse) => console.log(res.message)
      );
  }

  checkNameResult(result) {
    if (Array.isArray(result) && result.length) {
      return result.map(x => x.primaryName).join(', ');
    } else {
      return 'Result not found';
    }
  }

}
