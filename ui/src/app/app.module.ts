import 'hammerjs';
import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {FormsModule} from '@angular/forms';
import {HttpModule} from '@angular/http';
import {AppRoutingModule} from './app-routing.module';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';

// Component
import {AppComponent} from './app.component';
import {BlogComponent} from './blog/blog.component';
import {NotFoundComponent} from './not-found/not-found.component';
import {FooterComponent} from './footer/footer.component';

// Covalent
import {CovalentCoreModule, CovalentLayoutModule} from '@covalent/core';
import {CovalentHttpModule} from '@covalent/http';
import {CovalentHighlightModule} from '@covalent/highlight';
import {CovalentMarkdownModule} from '@covalent/markdown';
import {CovalentDynamicFormsModule} from '@covalent/dynamic-forms';
import {HeaderComponent} from './header/header.component';
import {ArticleListComponent} from './article-list/article-list.component';

@NgModule({
  declarations: [
    AppComponent,
    BlogComponent,
    NotFoundComponent,
    FooterComponent,
    HeaderComponent,
    ArticleListComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    // Covalent
    CovalentLayoutModule,
    CovalentCoreModule,
    CovalentHttpModule.forRoot(),
    CovalentHighlightModule,
    CovalentMarkdownModule,
    CovalentDynamicFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
