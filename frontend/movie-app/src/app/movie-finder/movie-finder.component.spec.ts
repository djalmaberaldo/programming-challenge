import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MovieFinderComponent } from './movie-finder.component';
import { FormsModule } from '@angular/forms';
import { NgxPaginationModule } from 'ngx-pagination';
import { HttpClientModule } from '@angular/common/http';
import { CastingBoxComponent } from '../casting-box/casting-box.component';

describe('MovieFinderComponent', () => {
  let component: MovieFinderComponent;
  let fixture: ComponentFixture<MovieFinderComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [FormsModule, NgxPaginationModule, HttpClientModule],
      declarations: [ MovieFinderComponent, CastingBoxComponent]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MovieFinderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
