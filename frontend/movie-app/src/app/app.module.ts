import { BrowserModule } from '@angular/platform-browser';
import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MovieFinderComponent } from './movie-finder/movie-finder.component';
import { HeaderBarComponent } from './header-bar/header-bar.component';
import { HttpClientModule } from '@angular/common/http';
import {NgxPaginationModule} from 'ngx-pagination'; // <-- import the module
import {FormsModule} from '@angular/forms';
import { CastingBoxComponent } from './casting-box/casting-box.component';

@NgModule({
  declarations: [
    AppComponent,
    CastingBoxComponent,
    MovieFinderComponent,
    HeaderBarComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule,
    HttpClientModule,
    NgxPaginationModule,
  ],
  providers: [],
  schemas: [ CUSTOM_ELEMENTS_SCHEMA ],
  bootstrap: [AppComponent]
})
export class AppModule { }
