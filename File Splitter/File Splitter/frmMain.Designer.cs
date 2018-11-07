namespace File_Splitter
{
    partial class frmMain
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.txtFile = new System.Windows.Forms.TextBox();
            this.btnBrowseFile = new System.Windows.Forms.Button();
            this.txtDirectoryOutput = new System.Windows.Forms.TextBox();
            this.btnBrowseDirectory = new System.Windows.Forms.Button();
            this.folderBrowserDialog1 = new System.Windows.Forms.FolderBrowserDialog();
            this.btnSplit = new System.Windows.Forms.Button();
            this.txtNumBytes = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            // 
            // txtFile
            // 
            this.txtFile.Location = new System.Drawing.Point(12, 12);
            this.txtFile.Name = "txtFile";
            this.txtFile.ReadOnly = true;
            this.txtFile.Size = new System.Drawing.Size(296, 27);
            this.txtFile.TabIndex = 0;
            this.txtFile.TabStop = false;
            this.txtFile.Text = "Browse file to split...";
            // 
            // btnBrowseFile
            // 
            this.btnBrowseFile.Location = new System.Drawing.Point(314, 11);
            this.btnBrowseFile.Name = "btnBrowseFile";
            this.btnBrowseFile.Size = new System.Drawing.Size(53, 27);
            this.btnBrowseFile.TabIndex = 1;
            this.btnBrowseFile.Text = "...";
            this.btnBrowseFile.UseVisualStyleBackColor = true;
            this.btnBrowseFile.Click += new System.EventHandler(this.btnBrowseFile_Click);
            // 
            // txtDirectoryOutput
            // 
            this.txtDirectoryOutput.Location = new System.Drawing.Point(12, 45);
            this.txtDirectoryOutput.Name = "txtDirectoryOutput";
            this.txtDirectoryOutput.ReadOnly = true;
            this.txtDirectoryOutput.Size = new System.Drawing.Size(296, 27);
            this.txtDirectoryOutput.TabIndex = 2;
            this.txtDirectoryOutput.TabStop = false;
            this.txtDirectoryOutput.Text = "Browse folder output...";
            // 
            // btnBrowseDirectory
            // 
            this.btnBrowseDirectory.Location = new System.Drawing.Point(314, 44);
            this.btnBrowseDirectory.Name = "btnBrowseDirectory";
            this.btnBrowseDirectory.Size = new System.Drawing.Size(53, 27);
            this.btnBrowseDirectory.TabIndex = 3;
            this.btnBrowseDirectory.Text = "...";
            this.btnBrowseDirectory.UseVisualStyleBackColor = true;
            this.btnBrowseDirectory.Click += new System.EventHandler(this.btnBrowseDirectory_Click);
            // 
            // btnSplit
            // 
            this.btnSplit.Location = new System.Drawing.Point(11, 111);
            this.btnSplit.Name = "btnSplit";
            this.btnSplit.Size = new System.Drawing.Size(355, 33);
            this.btnSplit.TabIndex = 4;
            this.btnSplit.Text = "Split";
            this.btnSplit.UseVisualStyleBackColor = true;
            this.btnSplit.Click += new System.EventHandler(this.btnSplit_Click);
            // 
            // txtNumBytes
            // 
            this.txtNumBytes.Location = new System.Drawing.Point(12, 78);
            this.txtNumBytes.Name = "txtNumBytes";
            this.txtNumBytes.Size = new System.Drawing.Size(227, 27);
            this.txtNumBytes.TabIndex = 5;
            this.txtNumBytes.Text = "1000";
            this.txtNumBytes.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(245, 81);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(121, 20);
            this.label1.TabIndex = 6;
            this.label1.Text = "Byte Increment";
            // 
            // frmMain
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(378, 157);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.txtNumBytes);
            this.Controls.Add(this.btnSplit);
            this.Controls.Add(this.btnBrowseDirectory);
            this.Controls.Add(this.txtDirectoryOutput);
            this.Controls.Add(this.btnBrowseFile);
            this.Controls.Add(this.txtFile);
            this.Font = new System.Drawing.Font("Cambria", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "frmMain";
            this.ShowIcon = false;
            this.ShowInTaskbar = false;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "File Splitter";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.TextBox txtFile;
        private System.Windows.Forms.Button btnBrowseFile;
        private System.Windows.Forms.TextBox txtDirectoryOutput;
        private System.Windows.Forms.Button btnBrowseDirectory;
        private System.Windows.Forms.FolderBrowserDialog folderBrowserDialog1;
        private System.Windows.Forms.Button btnSplit;
        private System.Windows.Forms.TextBox txtNumBytes;
        private System.Windows.Forms.Label label1;
    }
}

